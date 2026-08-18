# getAllDesktopShortcutInfo（系统接口）

## 导入模块

```TypeScript
```

## getAllDesktopShortcutInfo

```TypeScript
function getAllDesktopShortcutInfo(userId: number): Promise<Array<ShortcutInfo>>
```

查询指定用户的所有快捷方式信息。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_SHORTCUTS

<!--Device-shortcutManager-function getAllDesktopShortcutInfo(userId: int): Promise<Array<ShortcutInfo>>--><!--Device-shortcutManager-function getAllDesktopShortcutInfo(userId: int): Promise<Array<ShortcutInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ShortcutInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
