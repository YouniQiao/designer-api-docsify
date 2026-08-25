# debug

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: any[]): void
```

Prints DEBUG logs.DEBUG logs are not recorded in official versions by default. They are available in debug versions or in official versions with the debug function enabled.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | number | Yes |
| tag | string | Yes |
| format | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any[] | Yes |
