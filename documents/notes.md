División de Tareas para dos Desarrolladores
Para implementar eficientemente el reto "Terminal Souls", la división de tareas debe aprovechar el diseño modular del programa. Aquí se propone una distribución equilibrada:

1. 
Implementar generar_daño(min, max) con soporte para críticos (10% de doble daño).
Integrar el sistema de críticos en todos los ataques (extra). 
Desarrollar turno_jugador() con validación de pociones y habilidad especial (50% de fallo).
Implementar mostrar_estado() con barra de vida visual (ej: [#####---]).
Desarrollar turno_enemigo() con IA básica: atacar normalmente o curarse si HP < 20%.


2. 

Crear verificar_ganador(hp_h, hp_e) para finalizar el juego cuando HP <= 0.
Manejar todos los mensajes de consola (ej: "¡El Héroe golpea por 15!").u
Crear el bucle principal del juego con while y llamadas a turnos.
mejores prácticas simulador combate por turnos
