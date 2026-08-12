# setValue (System API)

## Modules to Import

```TypeScript
import { brightness } from '@kit.BasicServicesKit';
```

## setValue

```TypeScript
function setValue(value: number): void
```

Sets the screen brightness.

**Since:** 7

<!--Device-brightness-function setValue(value: int): void--><!--Device-brightness-function setValue(value: int): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [4700101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-brightness.md#4700101-service-connection-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    brightness.setValue(128);
} catch(err) {
    console.error('set brightness failed, err: ' + err);
}
```


## setValue

```TypeScript
function setValue(value: number, continuous: boolean): void
```

Sets the screen brightness. This API is used for continuous brightness adjustment. To achieve a better performance,set **continuous** to **true** when you start, and set it to **false** after you finish.

**Since:** 11

<!--Device-brightness-function setValue(value: int, continuous: boolean): void--><!--Device-brightness-function setValue(value: int, continuous: boolean): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| continuous | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [4700101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-brightness.md#4700101-service-connection-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    brightness.setValue(128, true);
} catch(err) {
    console.error('set brightness failed, err: ' + err);
}
```
