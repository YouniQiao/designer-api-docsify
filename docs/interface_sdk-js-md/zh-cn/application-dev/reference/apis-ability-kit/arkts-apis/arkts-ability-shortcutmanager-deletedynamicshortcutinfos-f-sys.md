# deleteDynamicShortcutInfos（系统接口）

## 导入模块

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## deleteDynamicShortcutInfos

```TypeScript
function deleteDynamicShortcutInfos(bundleName: string, appIndex: number, userId: number, ids?: Array<string>): Promise<void>
```

删除指定的动态快捷方式。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_SHORTCUTS or (ohos.permission.MANAGE_SHORTCUTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |
| userId | number | 是 |
| ids | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700070](../errorcode-bundle.md#17700070-指定的快捷方式id不合法) |
