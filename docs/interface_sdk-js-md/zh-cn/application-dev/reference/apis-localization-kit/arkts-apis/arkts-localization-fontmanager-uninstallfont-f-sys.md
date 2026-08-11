# uninstallFont（系统接口）

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<int>
```

根据字体名称从系统字体库中卸载已安装的字体文件。使用Promise异步回调。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**系统能力：** SystemCapability.Global.FontManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullName | string | 是 | 需要卸载的字体名称，可通过打开.ttf或.ttc字体文件获取。 &lt;br&gt;字体名称区分大小写，请确保与实际字体名称完全一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回卸载结果。 &lt;br&gt;- 返回0：卸载成功，字体已从系统字体库中移除。 &lt;br&gt;- 返回其他值：卸载失败，请根据错误码排查原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [31100107](../errorcode-font-manager.md#31100107-卸载的字体文件不存在) | Font file does not exist. |
| [31100108](../errorcode-font-manager.md#31100108-无法删除字体) | Font file delete error. |
| [31100109](../errorcode-font-manager.md#31100109-其他错误导致卸载失败) | Other error. |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Non-system application. |

