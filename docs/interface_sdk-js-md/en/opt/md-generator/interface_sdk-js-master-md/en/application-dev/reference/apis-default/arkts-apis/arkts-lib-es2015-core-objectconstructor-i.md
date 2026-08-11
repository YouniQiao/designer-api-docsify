# ObjectConstructor

## assign

```TypeScript
assign<T extends {}, U>(target: T, source: U): T & U
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

<!--Device-ObjectConstructor-assign<T extends {}, U>(target: T, source: U): T & U--><!--Device-ObjectConstructor-assign<T extends {}, U>(target: T, source: U): T & U-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| source | U | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T & U |

## assign

```TypeScript
assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

<!--Device-ObjectConstructor-assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V--><!--Device-ObjectConstructor-assign<T extends {}, U, V>(target: T, source1: U, source2: V): T & U & V-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| source1 | U | Yes |
| source2 | V | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T & U & V |

## assign

```TypeScript
assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

<!--Device-ObjectConstructor-assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W--><!--Device-ObjectConstructor-assign<T extends {}, U, V, W>(target: T, source1: U, source2: V, source3: W): T & U & V & W-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | T | Yes |
| source1 | U | Yes |
| source2 | V | Yes |
| source3 | W | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T & U & V & W |

## assign

```TypeScript
assign(target: object, ...sources: any[]): any
```

Copy the values of all of the enumerable own properties from one or more source objects to a target object. Returns the target object.

<!--Device-ObjectConstructor-assign(target: object, ...sources: any[]): any--><!--Device-ObjectConstructor-assign(target: object, ...sources: any[]): any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| sources | any[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

## getOwnPropertySymbols

```TypeScript
getOwnPropertySymbols(o: any): symbol[]
```

Returns an array of all symbol properties found directly on object o.

<!--Device-ObjectConstructor-getOwnPropertySymbols(o: any): symbol[]--><!--Device-ObjectConstructor-getOwnPropertySymbols(o: any): symbol[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| o | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| symbol[] |

## is

```TypeScript
is(value1: any, value2: any): boolean
```

Returns true if the values are the same value, false otherwise.

<!--Device-ObjectConstructor-is(value1: any, value2: any): boolean--><!--Device-ObjectConstructor-is(value1: any, value2: any): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value1 | any | Yes |
| value2 | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(o: {}): string[]
```

Returns the names of the enumerable string properties and methods of an object.

<!--Device-ObjectConstructor-keys(o: {}): string[]--><!--Device-ObjectConstructor-keys(o: {}): string[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| o | {} | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## setPrototypeOf

```TypeScript
setPrototypeOf(o: any, proto: object | null): any
```

Sets the prototype of a specified object o to object proto or null. Returns the object o.

<!--Device-ObjectConstructor-setPrototypeOf(o: any, proto: object | null): any--><!--Device-ObjectConstructor-setPrototypeOf(o: any, proto: object | null): any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| o | any | Yes |
| proto | object \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |
