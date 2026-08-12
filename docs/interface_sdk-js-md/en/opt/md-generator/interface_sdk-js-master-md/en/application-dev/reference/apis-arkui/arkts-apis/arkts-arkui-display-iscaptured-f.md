# isCaptured

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## isCaptured

```TypeScript
function isCaptured(): boolean
```

Checks whether the device's screen content is being captured.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function isCaptured(): boolean--><!--Device-display-function isCaptured(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let ret: boolean = false;
// Check whether the screen content is captured.
ret = display.isCaptured();
```


## isCaptured

```TypeScript
function isCaptured(bundleNameList: Array<string>): boolean
```

Check whether the device is captured, projected, or recorded by any app in the bundle name list.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean--><!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleNameList | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1400004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400004-parameter-error) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
try {
  const bundleList: Array<string> = ['com.example.app'];
  let ret = display.isCaptured(bundleList);
  console.info(`The screen is captured or not: ${ret}`);
} catch (err) {
  console.error(`Failed to get display isCaptured. Code: ${err.code}, message: ${err.message}`);
}
```
