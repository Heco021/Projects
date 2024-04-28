const { Client } = require('discord.js-selfbot-v13');
const { Worker } = require('worker_threads');
const keep_alive = require('./keep_alive.js');
const config = require('./config.json');
const pokename = require('./pokename.json');

const client = new Client();
const iSpam = new Worker('./iSpam.js');

client.on('ready', async () => {
	console.log('Bot ready!');
});

client.on('messageCreate', async (message) => {
	const userID = message.author.id;
	if (message.channel.id === config.channel_id) {
		if (message.embeds.length === 1 && userID === config.target_id && message.embeds[0].image) {
			message.channel.send(`<@${config.target_id}> hint`);
		} else if (userID === config.target_id && message.content.startsWith('The pokémon is ')) {
			const name = message.content.replace(/\\/g, '').slice(15, -1);
			const size = name.length;
			const temp = pokename[size.toString()];
			let names = [];
			for (let i of temp) {
				let key0 = true;
				for (let j = 0; j < size; j++) {
					if (name[j] === "_") {
						continue;
					} else if (name[j] !== i[j]) {
						key0 = false;
						break;
					}
				}
				if (key0) {
					names.push(i);
				}
			};
			for (let i of names) {
				await message.channel.send(`<@${config.target_id}> catch ${i}`);
				await new Promise(resolve => setTimeout(resolve, config.delay));
			}
		} else if (userID === config.target_id && message.content.startsWith(`Congratulations <@${config.alt_account_id}>! You caught a `)) {
			console.log(message.content);
		}
	} if (userID === config.main_account_id) {
		if (message.content.startsWith('!do ')) {
			await message.channel.send(message.content.slice(4));
		} else if (message.content === '!ping') {
			await message.channel.send(`Pong! ${Math.round(client.ws.ping)}ms`);
		}
	}
});

client.login(process.env.T);