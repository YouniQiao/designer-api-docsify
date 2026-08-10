# uninstallFont (System API)

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<int>
```

根据字体名称从系统字体库中卸载已安装的字体文件。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullName | string | Yes | 需要卸载的字体名称，可通过打开.ttf或.ttc字体文件获取。 &lt;br&gt;字体名称区分大小写，请确保与实际字体名称完全一致。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回卸载结果。 &lt;br&gt;- 返回0：卸载成功，字体已从系统字体库中移除。 &lt;br&gt;- 返回其他值：卸载失败，请根据错误码排查原因。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 31100107 | Font file does not exist. |
| 31100108 | Font file delete error. |
| 31100109 | Other error. |
| 201 | Permission denied. |
| 202 | Non-system application. |

