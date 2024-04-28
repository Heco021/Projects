const { Client } = require('discord.js-selfbot-v13');
const { parentPort } = require('worker_threads');

const client = new Client();

let spamChannel;
const config = require('./config.json');
const T = require("/data/data/com.termux/files/home/TOKEN.json");

client.on('ready', () => {
	spamChannel = client.channels.cache.get(config.channel_id);
	console.log('spamFunction ready!');
});

client.on('messageCreate', (message) => {
	if (message.author.id === config.main_account_id && message.content === '!bot') {
		iSpam();
	}
});

async function iSpam() {
	while (true) {
		await spamChannel.send("E");
		await new Promise(resolve => setTimeout(resolve, config.delay));
	}
};

client.login(T.T);