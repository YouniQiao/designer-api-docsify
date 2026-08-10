# isCaptured

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## isCaptured

```TypeScript
function isCaptured(): boolean
```

检查设备的屏幕显示信息是否被获取。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function isCaptured(): boolean--><!--Device-display-function isCaptured(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | boolean值，返回设备的屏幕显示信息是否存在被获取的情况。返回true表示设备的屏幕信息存在被获取的情况，可能为：设备正处于截屏、投屏、录屏状态，或已创建虚拟屏幕(虚拟屏幕可能被应用获 取屏幕图像)；返回false则表示设备的屏幕信息不存在被获取的情况。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

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

检查该设备是否被bundle名称列表中的任何应用抓拍、投影或录制。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean--><!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleNameList | Array&lt;string&gt; | Yes | 需要检查的应用包名称列表。数组的最大大小为100。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示该设备包名称列表中的任何应用捕获、投影或录制。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400004 | Parameter error. Possible cause: 1.The size of bundleNameList is larger than 100. |
| 1400003 | This display manager service works abnormally. |

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

