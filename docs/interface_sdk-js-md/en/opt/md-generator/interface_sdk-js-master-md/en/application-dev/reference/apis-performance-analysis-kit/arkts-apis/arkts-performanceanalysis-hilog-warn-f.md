# warn

## Modules to Import

```TypeScript
```

## warn

```TypeScript
function warn(domain: number, tag: string, format: string, ...args: any[]): void
```

Prints WARN logs.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hilog-function warn(domain: number, tag: string, format: string, ...args: any[]): void--><!--Device-hilog-function warn(domain: number, tag: string, format: string, ...args: any[]): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | number | Yes |
| tag | string | Yes |
| format | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any[] | Yes |

**Examples**

This example is used to output a WARN log with the format string being "%{public}s World %{private}d". The variable  is a plaintext string, and the variable  is a private integer.

```TypeScript
hilog.warn(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

If "hello" is filled in %{public}s and 3 in %{private}d, the output log is as follows:

```TypeScript
08-05 12:21:47.579  2695-2703  A00001/testTag  com.example.hilogDemo  W     hello World <private>
```


## warn

```TypeScript
function warn(domain: number, tag: string, format: string, ...args: RecordData[]): void
```

Prints WARN logs.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hilog-function warn(domain: int, tag: string, format: string, ...args: RecordData[]): void--><!--Device-hilog-function warn(domain: int, tag: string, format: string, ...args: RecordData[]): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | number | Yes |
| tag | string | Yes |
| format | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)[] | Yes |
