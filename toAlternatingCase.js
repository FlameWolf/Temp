/**
 * Method to turn text into alternative uppercase/lowercase characters.
 * Exmple: "Hello World!" => "hElLo WoRlD!"
 */
const toAlternatingCase = input => {
	let isUpperNext = true;
	return input.replace(/\p{L}/gu, char => ((isUpperNext = !isUpperNext) ? char.toUpperCase() : char.toLowerCase()));
};