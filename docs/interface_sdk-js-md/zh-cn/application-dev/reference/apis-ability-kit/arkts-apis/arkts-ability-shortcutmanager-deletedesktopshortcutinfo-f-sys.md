# deleteDesktopShortcutInfo（系统接口）

## 导入模块

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## deleteDesktopShortcutInfo

```TypeScript
function deleteDesktopShortcutInfo(shortcutInfo: ShortcutInfo, userId: number): Promise<void>
```

删除指定用户的快捷方式信息。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_SHORTCUTS

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
