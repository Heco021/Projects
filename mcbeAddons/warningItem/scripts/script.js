// Define the items that trigger the warning
const ITEMS_TO_CHECK = ["minecraft:diamond", "minecraft:emerald"];

// Define the warning message
const WARNING_MESSAGE = "Warning: Holding a valuable item in the overworld is not allowed! Drop it immediately.";

// Function to check if the player is holding any of the specified items
function checkHeldItems(player) {
	const mainHandItem = player.getComponent("minecraft:hand_container").data[0].item;
	if (mainHandItem && ITEMS_TO_CHECK.includes(mainHandItem.__identifier__)) {
		// Send warning message to the player
		system.executeCommand(`tellraw "${player.id}" {"rawtext":[{"text":"${WARNING_MESSAGE}"}]}`);
	}
}

// Listen for tick events
system.listenForEvent("minecraft:entity_tick", (eventData) => {
	// Check if the entity is a player
	if (eventData.data.entity.__identifier__ === "minecraft:player") {
		// Get the player entity
	const player = eventData.data.entity;

		// Check if the player is in the overworld
		if (eventData.data.dimension === "overworld") {
			// Check if the player is holding any of the specified items
			checkHeldItems(player);
		}
	}
});