# 🧠 Análisis del código de Bitcoin v0.1

Explorar el código de **Bitcoin v0.1** es como revisar el primer plano de una máquina que hoy mueve miles de millones en el mundo digital; fue publicado por **Satoshi Nakamoto** en 2009 y tiene un aire experimental que combina visión con simplicidad [1].  
Lo primero que salta a la vista es lo compacto del código: todo está metido en unos pocos archivos y sin modularidad clara, como si se tratara de un prototipo funcional más que de un sistema listo para escalar.

En esa versión inicial, por ejemplo, se podían enviar bitcoins directamente a una **IP**, algo que hoy sería impensable por razones de seguridad y descentralización.  
También hay ausencia de **pruebas automatizadas** y ni hablar de documentación completa. Los comentarios son escasos y el manejo de errores muy limitado.  
Sin embargo, eso no le resta valor al trabajo: en ese momento, la idea era probar que el sistema **podía funcionar**, no que fuera perfecto [2].

Lo que sí es impresionante es cómo ya estaba integrada la lógica de los **scripts** que permiten ejecutar condiciones dentro de las transacciones, lo que luego sería clave para sistemas como **Lightning Network** o contratos simples.  
También aparece la codificación **Base58** para las direcciones, algo muy bien pensado porque evita errores humanos con letras que se parecen, como la '0' y la 'O' [3].

---

## 🔍 Curiosidades y detalles pequeños (pero relevantes)

- 🧮 El valor `nValue` se dividía entre `CENT` para convertir satoshis a bitcoins dentro de la interfaz.
- ⛏️ El tiempo de maduración de la recompensa minera era de **120 bloques** (hoy es 100) [4].
- 📁 Hay una carpeta llamada `nov08` que contiene versiones previas antes del lanzamiento oficial.
- 🔗 El sistema permitía enviar BTC directamente a una **dirección IP**, funcionalidad luego eliminada.
- 🛡️ Las conexiones se hacían sin cifrado ni verificación de identidad, propio de una red experimental.

---

## 🧾 Conclusión

Esta versión 0.1 de Bitcoin representa más una **idea que un producto pulido**.  
Sus imperfecciones lo hacen interesante porque muestran el punto de partida real de una de las tecnologías más influyentes de nuestro tiempo.  
Observarlo con atención permite entender muchas decisiones que los desarrolladores tomaron después [1][2][4].  
Es un fragmento de historia viva, escrito en **C++**, sin tests, sin frameworks modernos, pero con una visión clara de lo que podía llegar a ser.

---

## 📚 Referencias (formato IEEE)

[1] S. Nakamoto, *Bitcoin v0.1*, GitHub, [Repositorio de código], 2009.  
[2] A. B. Antonopoulos, *Mastering Bitcoin: Unlocking Digital Cryptocurrencies*, 2nd ed., O’Reilly Media, 2017.  
[3] N. Szabo, “Formalizing and Securing Relationships on Public Networks,” *First Monday*, vol. 2, no. 9, 1997.  
[4] J. Bonneau, A. Narayanan, A. Miller, J. Clark, E. W. Felten, and S. Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press, 2016.  
