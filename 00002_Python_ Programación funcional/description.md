Defina una función llamada `composicion` que reciba 3 argumentos, en el siguiente orden:

* Un número, `x`
* Una función, `f`
* Otra función, `g`

Nota: Las funciones `f` y `g` tienen apenas un argumento numérico cada una. Por ejemplo, _f(x) = 2x_ y _g(x) = x+3_.

Además, la función `composicion` debe, aplicar _f_ a _x_ y, en seguida, aplicar _g_ sobre el resultado. Matemáticamente, esto equivale a _g(f(x))_.

Siguiendo el ejemplo donde _f(x)=2x_ y _g(x)=x+3_, entonces `composicion(7,f,g)` debería resultar en **17**, ya que el doble de 7 es 14, que al sumarle 3, resulta en 17.

> Defina una función `composicion` que:

> 1. Tome a `x`, `f` y `g` como argumentos.
> 2. Aplique la función `f` al número `x`.
> 3. Aplique la función `g` al resultado del punto 2.
> 4. Devuelva el resultado del punto 3.

