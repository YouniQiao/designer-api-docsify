# on (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## on('enabledAccessibilityExtensionListChange')

```TypeScript
function on(type: 'enabledAccessibilityExtensionListChange', callback: Callback<void>): void
```

Adds a listener for changes in the list of enabled accessibility extension abilities. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function on(type: 'enabledAccessibilityExtensionListChange', callback: Callback<void>): void--><!--Device-config-function on(type: 'enabledAccessibilityExtensionListChange', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'enabledAccessibilityExtensionListChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { config } from '@kit.AccessibilityKit';

config.on('enabledAccessibilityExtensionListChange', () => {
  console.info('subscribe enabled accessibility extension list change state success');
});
```


## on('installedAccessibilityListChange')

```TypeScript
function on(type: 'installedAccessibilityListChange', callback: Callback<void>): void
```

Adds a listener for changes in the list of installed accessibility extension abilities. This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function on(type: 'installedAccessibilityListChange', callback: Callback<void>): void--><!--Device-config-function on(type: 'installedAccessibilityListChange', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'installedAccessibilityListChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { config } from '@kit.AccessibilityKit';

config.on('installedAccessibilityListChange', () => {
  console.info('subscribe installed accessibility extension list change state success');
});
```
