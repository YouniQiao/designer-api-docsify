# uninstallFont（系统接口）

## uninstallFont

```TypeScript
function uninstallFont(fullName: string): Promise<number>
```

根据字体名称从系统字体库中卸载已安装的字体文件。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>--><!--Device-fontManager-function uninstallFont(fullName: string): Promise<int>-End-->

**系统能力：** SystemCapability.Global.FontManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [31100107](../errorcode-font-manager.md#31100107-卸载的字体文件不存在) |
| [31100108](../errorcode-font-manager.md#31100108-无法删除字体) |
| [31100109](../errorcode-font-manager.md#31100109-其他错误导致卸载失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
