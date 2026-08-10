# DateConstructor

**ArkTS mode:** ArkTS-Dyn only

## UTC

```TypeScript
UTC(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): number
```

Returns the number of milliseconds between midnight, January 1, 1970 Universal Coordinated Time (UTC) (or GMT) and the specified date.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-DateConstructor-UTC(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): number--><!--Device-DateConstructor-UTC(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | number | Yes |  |
| monthIndex | number | Yes |  |
| date | number | No |  |
| hours | number | No |  |
| minutes | number | No |  |
| seconds | number | No |  |
| ms | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## [[Call]]

```TypeScript
(): string
```

**ArkTS mode:** ArkTS-Dyn only

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## [[Construct]]

```TypeScript
new(): Date
```

**ArkTS mode:** ArkTS-Dyn only

**Return value:**

| Type | Description |
| --- | --- |
| Date |  |

## [[Construct]]

```TypeScript
new(value: number | string): Date
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Date |  |

## [[Construct]]

```TypeScript
new(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): Date
```

Creates a new Date.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-DateConstructor-new(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): Date--><!--Device-DateConstructor-new(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): Date-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| year | number | Yes |  |
| monthIndex | number | Yes |  |
| date | number | No |  |
| hours | number | No |  |
| minutes | number | No |  |
| seconds | number | No |  |
| ms | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Date |  |

## now

```TypeScript
now(): number
```

Returns the number of milliseconds elapsed since midnight, January 1, 1970 Universal Coordinated Time (UTC).

**ArkTS mode:** ArkTS-Dyn only

<!--Device-DateConstructor-now(): number--><!--Device-DateConstructor-now(): number-End-->

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## parse

```TypeScript
parse(s: string): number
```

Parses a string containing a date, and returns the number of milliseconds between that date and midnight, January 1, 1970.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-DateConstructor-parse(s: string): number--><!--Device-DateConstructor-parse(s: string): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## prototype

```TypeScript
readonly prototype: Date
```

**Type:** Date

**ArkTS mode:** ArkTS-Dyn only

