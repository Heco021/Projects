const { Client } = require('discord.js-selfbot-v13');
const { parentPort } = require('worker_threads');

const client = new Client();

let spamChannel;
const config = require('./config.json');

client.on('ready', () => {
	spamChannel = client.channels.cache.get(config.channel_id);
	console.log('spamFunction started!');
	iSpam();
});

async function iSpam() {
	while (true) {
		await spamChannel.send("E");
		await new Promise(resolve => setTimeout(resolve, config.delay));
	}
};

client.login(process.env.T);