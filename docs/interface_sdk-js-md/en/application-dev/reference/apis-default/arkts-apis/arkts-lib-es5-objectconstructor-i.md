# ObjectConstructor

## Modules to Import

```TypeScript
```

## [[Call]]

```TypeScript
(): any
```

**Return value:**

| Type | Description |
| --- | --- |
## [[Call]]

```TypeScript
(value: any): any
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## [[Construct]]

```TypeScript
new(value?: any): Object
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## create

```TypeScript
create(o: object | null): any
```

Creates an object that has the specified prototype or that has null prototype.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | object \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## create

```TypeScript
create(o: object | null, properties: PropertyDescriptorMap & ThisType<any>): any
```

Creates an object that has the specified prototype, and that optionally contains specified properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | object \| null | Yes |  |
| properties | PropertyDescriptorMap & ThisType & lt;any & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defineProperties

```TypeScript
defineProperties<T>(o: T, properties: PropertyDescriptorMap & ThisType<any>): T
```

Adds one or more properties to an object, and/or modifies attributes of existing properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |
| properties | PropertyDescriptorMap & ThisType & lt;any & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defineProperty

```TypeScript
defineProperty<T>(o: T, p: PropertyKey, attributes: PropertyDescriptor & ThisType<any>): T
```

Adds a property to an object, or modifies attributes of an existing property.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |
| p | [PropertyKey](arkts-propertykey-t.md) | Yes |  |
| attributes | PropertyDescriptor & ThisType & lt;any & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## freeze

```TypeScript
freeze<T extends Function>(f: T): T
```

Prevents the modification of existing property attributes and values, and prevents the addition of new properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| f | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## freeze

```TypeScript
freeze<T extends {[idx: string]: U | null | undefined | object}, U extends string | bigint | number | boolean | symbol>(o: T): Readonly<T>
```

Prevents the modification of existing property attributes and values, and prevents the addition of new properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## freeze

```TypeScript
freeze<T>(o: T): Readonly<T>
```

Prevents the modification of existing property attributes and values, and prevents the addition of new properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getOwnPropertyDescriptor

```TypeScript
getOwnPropertyDescriptor(o: any, p: PropertyKey): PropertyDescriptor | undefined
```

Gets the own property descriptor of the specified object. An own property descriptor is one that is defined directly on the object and is not inherited from the object's prototype.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |
| p | [PropertyKey](arkts-propertykey-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getOwnPropertyNames

```TypeScript
getOwnPropertyNames(o: any): string[]
```

Returns the names of the own properties of an object. The own properties of an object are those that are defined directly on that object, and are not inherited from the object's prototype. The properties of an object include both fields (objects) and functions.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## getPrototypeOf

```TypeScript
getPrototypeOf(o: any): any
```

Returns the prototype of an object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## isExtensible

```TypeScript
isExtensible(o: any): boolean
```

Returns a value that indicates whether new properties can be added to an object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## isFrozen

```TypeScript
isFrozen(o: any): boolean
```

Returns true if existing property attributes and values cannot be modified in an object, and new properties cannot be added to the object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## isSealed

```TypeScript
isSealed(o: any): boolean
```

Returns true if existing property attributes cannot be modified in an object and new properties cannot be added to the object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## keys

```TypeScript
keys(o: object): string[]
```

Returns the names of the enumerable string properties and methods of an object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | object | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## preventExtensions

```TypeScript
preventExtensions<T>(o: T): T
```

Prevents the addition of new properties to an object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## seal

```TypeScript
seal<T>(o: T): T
```

Prevents the modification of attributes of existing properties, and prevents the addition of new properties.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| o | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## prototype

```TypeScript
readonly prototype: Object
```

A reference to the prototype for a class of objects.

**Type:** Object
