#include <dpp/dpp.h>
#include <fstream>
#include <nlohmann/json.hpp>

nlohmann::json T;
std::ifstream file("/data/data/com.termux/files/home/TOKEN.json");

class Await {
	bool check = true;
public:
	void next() {
		check = false;
	}
	void await() {
		while (check) {}
		check = true;
	}
};

int main() {
	if (!file.is_open()) {
		std::cerr << "Failed to open file!";
		return 1;
	} 

	try {
		file >> T;
		file.close();
	} catch (const std::exception& e) {
		std::cerr << "Failed to parse JSON.\n" << e.what();
		return 1;
	}
	
	dpp::cluster bot(T["B"], dpp::i_default_intents);
	bot.on_log(dpp::utility::cout_logger());
	
	bot.on_slashcommand([&bot](const dpp::slashcommand_t& event) {
		if (event.command.usr.id == "870748995872518155") {
			if (event.command.get_command_name() == "async") {
				const dpp::snowflake channelID = event.command.channel_id;
				Await await;
				
				std::cout << "check1" << std::endl;
				bot.channel_get(channelID, [&bot, &await, channelID](const dpp::confirmation_callback_t& callback) {
					const dpp::channel channel = callback.get<dpp::channel>();
					Await await2;
					
					std::cout << "0-down1" << std::endl;
					bot.channel_get(channelID, [&await2](const dpp::confirmation_callback_t& callback) {
						const dpp::channel channel = callback.get<dpp::channel>();
						std::cout << "sub1" << std::endl;
						await2.next();
					});
					await2.await();
					
					std::cout << "0-down2" << std::endl;
					bot.channel_get(channelID, [&await2](const dpp::confirmation_callback_t& callback) {
						const dpp::channel channel = callback.get<dpp::channel>();
						std::cout << "sub2" << std::endl;
						await2.next();
					});
					await2.await();
					
					await.next();
				});
				await.await();
				
				std::cout << "check2" << std::endl;
				bot.channel_get(channelID, [&await](const dpp::confirmation_callback_t& callback) {
					const dpp::channel channel = callback.get<dpp::channel>();
					std::cout << "1-down1" << std::endl;
					await.next();
				});
				await.await();
				
				std::cout << "check3" << std::endl;
				event.reply("check3");
			}
		}
	});
	
	bot.on_ready([&bot](dpp::ready_t event) {
		if (dpp::run_once<struct register_bot_commands>()) {
			//bot.global_bulk_command_delete();
			bot.global_command_create(dpp::slashcommand("async", "async test", bot.me.id));
		}
	});
	
	bot.start(dpp::st_wait);
}