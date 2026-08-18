# EventProcess

```TypeScript
type EventProcess = (event: string, args: Record<string, Object>) => void
```

The general process funcation with an event and arguments.

**Since:** 26.1.0

<!--Device-avSession-type EventProcess = (event: string, args: Record<string, Object>) => void--><!--Device-avSession-type EventProcess = (event: string, args: Record<string, Object>) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | Yes |
