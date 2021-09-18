console.log("------- S T A R T --------");
//imports
const Discord = require('discord.js');
const FS = require('fs');

//read token
const readToken = FS.readFileSync('src/token.env').toString();
console.log(readToken);

//setup discord client
const client = new Discord.Client({intents: [Discord.Intents.FLAGS.GUILDS]});

//create client on ready message
client.on('ready', () => {
	console.log('ready');
});

//start discord bot
(async () => {
	client.login(readToken);
})();

console.log("-----E N D------")
