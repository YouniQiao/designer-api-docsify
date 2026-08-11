# installFont（系统接口）

## installFont

```TypeScript
function installFont(path: string): Promise<number>
```

将指定路径下的字体文件安装到系统字体库中。使用Promise异步回调。安装成功后，应用可以通过字体名称使用该字体。

**起始版本：** 19

**需要权限：** ohos.permission.UPDATE_FONT

<!--Device-fontManager-function installFont(path: string): Promise<int>--><!--Device-fontManager-function installFont(path: string): Promise<int>-End-->

**系统能力：** SystemCapability.Global.FontManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [31100106](../errorcode-font-manager.md#31100106-其他错误导致安装失败) |
| [31100104](../errorcode-font-manager.md#31100104-字体文件已安装) |
| [31100105](../errorcode-font-manager.md#31100105-已安装字体文件超过最大数量) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [31100102](../errorcode-font-manager.md#31100102-字体文件不支持安装) |
| [31100103](../errorcode-font-manager.md#31100103-字体文件拷贝失败) |
| [31100101](../errorcode-font-manager.md#31100101-字体文件不存在) |
