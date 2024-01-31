// Kirjoita ohjelma, joka tulostaa luvut 1-100. Tulosta kolmella jaollisten kohdalla luvun sijasta sana "Kossu" ja viidellä jaollisten "Vissy". Jos luku on jaollinen kolmella ja viidellä, tulosta KossuVissy.


const N = 100

function DivisibilityChecker(n){
	// Checks variable divisibility with 3, 5 or both and prints altered variable accordingly
	for(let i = 1; i <= n; i++){
		if(i % 3 == 0 && i % 5 == 0){
			console.log('KossuVichy');
		}
		else if(i % 5 == 0){
			console.log('Vichy')
		}
		else if(i % 3 != 0){
			console.log('Kossu');
		}
		else{
			console.log(i)
		}
	}
}
DivisibilityChecker(N)
