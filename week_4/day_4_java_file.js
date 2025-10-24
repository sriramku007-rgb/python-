// 1. var
// Scope: Function-scoped (visible within the entire function).
// Re-declaration: Allowed.
// Re-assignment: Allowed.
// Hoisting: Yes, but initialized as undefined.

var x = 5;
var y = 6;
var z = x + y;
console.log(z)
// 2. let
// Scope: Block-scoped (only available inside {} where defined).
// Re-declaration: Not allowed in the same scope.
// Re-assignment: Allowed.
// Hoisting: Yes, but not initialized (can’t use before declaration → “Temporal Dead Zone”).
let a="Hello World";
let b="welcome"
console.log(b);


// 3. const
// Scope: Block-scoped.
// Re-declaration: Not allowed.
// Re-assignment: ❌ Not allowed.
// Must be initialized at the time of declaration.

const message = 123456789;
console.log(message);


