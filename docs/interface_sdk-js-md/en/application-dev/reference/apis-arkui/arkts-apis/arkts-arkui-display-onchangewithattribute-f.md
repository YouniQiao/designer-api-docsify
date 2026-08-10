# onChangeWithAttribute

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## onChangeWithAttribute

```TypeScript
function onChangeWithAttribute(displayAttributeOption: Array<string>, callback: Callback<long>): void
```

开启显示设备指定属性变化的监听。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-display-function onChangeWithAttribute(displayAttributeOption: Array<string>, callback: Callback<long>): void--><!--Device-display-function onChangeWithAttribute(displayAttributeOption: Array<string>, callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayAttributeOption | Array&lt;string&gt; | Yes | 指定需要监听的屏幕属性名称，且仅限于 [display属性](../../../reference/apis-arkui/js-apis-display.md#属性)中包含的属性。 |
| callback | ArkTS-Dyn: [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | 回调函数。返回监听到的屏幕ID，该参数为整数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function onChangeWithAttribute can not work correctly due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. Possible causes: Internal IPC error. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let attributesChangeCallback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};
let attributes: Array<string> = ["rotation", "width"];
display.onChangeWithAttribute(attributes, attributesChangeCallback);
```

