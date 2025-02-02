const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			auth: false, //estado de autenticacion, usiario no logueado entonces falo
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			personajes: [],  // Lista vacía para personajes
			favoritos_planetas: [],
			favoritos_personajes: [],
			favoritos: [], //lisa vacia apra agregar personajes favoritos
			planetas: [],
			vehiculos: [],
		},
		actions: {

			loadPersonajes: async () => {
				try {
					const response = await fetch('https://www.swapi.tech/api/people'); // Llamo a la API
					const data = await response.json();
					setStore({ personajes: data.results }); // Guardo los personajes en el store
				} catch (error) {
					console.error("Error loading personajes:", error);
				}
			},

			setFavoritos_personajes: (personaje) => {
				const store = getStore();
				setStore({ favoritos_personajes: [...store.favoritos_personajes, personaje] });
			},


			loadPlanets: async () => {
				try {
					const response = await fetch('https://www.swapi.tech/api/planets'); // Llamo a la API
					const data = await response.json();
					setStore({ planetas: data.results }); // Guardo los personajes en el store
				} catch (error) {
					console.error("Error loading planetas:", error);
				}
			},

			setFavoritos_planetas: (planeta) => {
				const store = getStore();
				setStore({ favoritos_planetas: [...store.favoritos_planetas, planeta] });
			},



			loadVehiculos: async () => {
				try {
					const response = await fetch('https://www.swapi.tech/api/vehicles'); // Llamo a la API
					const data = await response.json();
					setStore({ vehiculos: data.results }); // Guardo los personajes en el store
				} catch (error) {
					console.error("Error loading vehiculos:", error);
				}
			},

			setVehiculos: (vehiculo) => {
				const store = getStore()
				setStore({ vehiculos: [...store.vehiculos, vehiculo] });

			},


			setFavoritos: (favorito) => {
				const store = getStore();
				setStore({ favoritos: [...store.favoritos, favorito] });
			},


			removeFavorito: (favorito) => {
				const store = getStore();
				const updatedFavoritos = store.favoritos.filter((item) => item !== favorito);
				setStore({ favoritos: updatedFavoritos });
			},

			// Use getActions to call a function within a fuction
			login: async (correo, contraseña) => {


				const myHeaders = new Headers();
				myHeaders.append("Content-Type", "application/json");

				const raw = JSON.stringify({
					"correo": correo,
					"contraseña": contraseña
				});

				const requestOptions = {
					method: "POST",
					headers: myHeaders,
					body: raw,
					redirect: "follow"
				};

				try {
					const response = await fetch(process.env.BACKEND_URL + "/api/login", requestOptions);
					const result = await response.json();

					if (response.status === 200) {
						localStorage.setItem("token", result.access_token);
						setStore({ auth: true });  // <-- Asegurar que el usuario está autenticado
						return true;
					} else {
						setStore({ auth: false });
						return false;
					}
					
				} catch (error) {
					console.error(error);
					return false;
				};
			},
			getProfile: async () => {
				let token = localStorage.getItem("token")
				try {
					const response = await fetch("https://potential-spork-7pvx7qxxxj9c64x-3001.app.github.dev/api/profile", {
						method: "GET",
						headers: {
							"Authorization": `Bearer ${token}`
						},
					});
					const result = await response.json();
					console.log(result)
				} catch (error) {
					console.error(error);
				};
			},

		tokenVerify: async () => {
	const token = localStorage.getItem("token");
	if (!token) {
		setStore({ auth: false });
		return false;
	}

	try {
		const response = await fetch(process.env.BACKEND_URL + "/api/token-verify", {
			method: "GET",
			headers: {
				"Authorization": `Bearer ${token}`
			},
		});
		if (response.status === 200) {
			setStore({ auth: true });
			return true;
		} else {
			setStore({ auth: false });
			localStorage.removeItem("token");
			return false;
		}
	} catch (error) {
		console.error("Error verificando el token:", error);
		setStore({ auth: false });
		localStorage.removeItem("token");
		return false;
	}
},

			//crear un nuevo endpoint que se llame verificacion de token
			//la peticion en la funcion tokenVerify del front deberia actualizar un estado auth:
			// },
			logout: () => {
				localStorage.removeItem("token");
				setStore({ auth: false, favoritos: [], favoritos_personajes: [], favoritos_planetas: [] }); 
				return true;
			},
			
			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;



