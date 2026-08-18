# addDesktopShortcutInfo（系统接口）

## 导入模块

```TypeScript
```

## addDesktopShortcutInfo

```TypeScript
function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: number): Promise<void>
```

增加指定用户的快捷方式信息。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_SHORTCUTS

<!--Device-shortcutManager-function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: int): Promise<void>--><!--Device-shortcutManager-function addDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shortcutInfo | [ShortcutInfo](arkts-ability-shortcutinfo-i.md) | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700070](../errorcode-bundle.md#17700070-指定的快捷方式id不合法) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
