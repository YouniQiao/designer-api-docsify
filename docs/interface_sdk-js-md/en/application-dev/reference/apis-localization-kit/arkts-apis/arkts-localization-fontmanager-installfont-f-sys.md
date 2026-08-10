# installFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## installFont

```TypeScript
function installFont(path: string): Promise<int>
```

将指定路径下的字体文件安装到系统字体库中。使用Promise异步回调。安装成功后，应用可以通过字体名称使用该字体。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function installFont(path: string): Promise<int>--><!--Device-fontManager-function installFont(path: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待安装的字体文件路径，仅支持.ttf和.ttc格式的字体文件。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回安装结果。 &lt;br&gt;- 返回0：安装成功，字体已添加到系统字体库。 &lt;br&gt;- 返回其他值：安装失败，请根据错误码排查原因。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 31100106 | Other error. |
| 31100104 | Font file installed. |
| 31100105 | Exceeded maximum number of installed files. |
| 201 | Permission denied. |
| 202 | Non-system application. |
| 31100102 | Font is not supported. |
| 31100103 | Font file copy failed. |
| 31100101 | Font does not exist. |

