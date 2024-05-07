#!/bin/bash

if [ -z "$1" ]; then
	echo "Please provide a file or directory as input."
	exit 1
fi

target="$1"

# Check if input exists
if [ ! -e "$target" ]; then
	echo "The input '$target' does not exist."
	exit 1
fi

keep() {
	local file1=$1
	local file2=$2
	local size1=$(stat -c%s "$file1")
	local size2=$(stat -c%s "$file2")
	echo "$file1 -> $size1"
	echo "$file2 -> $size2"
	if [[ $size1 -le $size2 ]]; then
		first="$file1"
		rm "$file2" -f
		echo "$file2 -> Has been removed."
	else
		first="$file2"
		rm "$file1" -f
		echo "$file1 -> Has been removed."
	fi
	echo -e ""
}

remove() {
	list=("zip" "7z" "tar" "bz2" "tar.bz2" "gz" "tar.gz" "xz" "tar.xz" "lz4" "tar.lz4" "zst" "tar.zst")
	for format in "${list[@]}"; do
		if [[ -e "$file.$format" ]]; then
			rm "$file.$format" -f
			echo "$file.$format -> Has been removed."
		fi
	done
	echo -e ""
}

if [[ -f $target ]]; then
	type="file"
elif [[ -d $target ]]; then
	type="directory"
	target=$(basename "$target")
else
	echo "Please enter an input!"
	exit 1
fi

masterDir="$HOME/.compressZone"
#masterDir="/storage/emulated/0/Documents"
location=$(pwd)

if [[ "$target" == "." ]]; then
	setTarget=.
	setTarget2=*
	target="$(basename $(pwd))"
	type="directory"
else
	setTarget="$target"
fi
file=$masterDir/$target

remove

zip "$file.zip" "$setTarget" -9qr
first="$file.zip"
7z a "$file.7z" "$setTarget" -mmt1 -mx9 -r -bb0 -bsp0 -bso0
keep "$first" "$file.7z"

if [[ $type == "file" ]]; then
	bzip2 "$target" -9kc > "$file.bz2"
	keep "$first" "$file.bz2"
	gzip "$target" -9kc > "$file.gz"
	keep "$first" "$file.gz"
	xz "$target" -9kc > "$file.xz"
	keep "$first" "$file.xz"
	lz4 "$target" -12c > "$file.lz4"
	keep "$first" "$file.lz4"
	zstd "$target" -22c --ultra > "$file.zst"
	keep "$first" "$file.zst"
else
	tar -cf "$file.tar" $setTarget2
	bzip2 "$file.tar" -9kc > "$file.tar.bz2"
	keep "$first" "$file.tar.bz2"
	gzip "$file.tar" -9kc > "$file.tar.gz"
	keep "$first" "$file.tar.gz"
	xz "$file.tar" -9kc > "$file.tar.xz"
	keep "$first" "$file.tar.xz"
	lz4 "$file.tar" -12c > "$file.tar.lz4"
	keep "$first" "$file.tar.lz4"
	zstd "$file.tar" -22c --ultra > "$file.tar.zst"
	keep "$first" "$file.tar.zst"
	rm "$file.tar"
fi
if [[ -e $(basename "$first") ]]; then
	read -p "The file '$(basename "$first")' already exist in your current directory.
Please rename the file and press enter to continue if you don't to overwrite the file."
fi
mv "$first" "$location"