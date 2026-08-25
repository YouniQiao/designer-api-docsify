# isScreenLocked

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## isScreenLocked

```TypeScript
function isScreenLocked(callback: AsyncCallback<boolean>): void
```

Checks whether the screen is currently locked.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.MiscServices.ScreenLock

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isScreenLocked

```TypeScript
function isScreenLocked(): Promise<boolean>
```

Checks whether the screen is currently locked.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.MiscServices.ScreenLock

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
