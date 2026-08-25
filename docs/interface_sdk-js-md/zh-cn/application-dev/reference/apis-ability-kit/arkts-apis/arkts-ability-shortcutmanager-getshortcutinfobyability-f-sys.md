# getShortcutInfoByAbility（系统接口）

## 导入模块

```TypeScript
import { shortcutManager } from 'kits/@kit.AbilityKit';
```

## getShortcutInfoByAbility

```TypeScript
function getShortcutInfoByAbility(bundleName: string, moduleName: string, abilityName: string, userId?: number, appIndex?: number): Array<ShortcutInfo>
```

查询指定用户下指定UIAbility的快捷方式信息。

**起始版本：** 24

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| abilityName | string | 是 |
| userId | number | 否 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;ShortcutInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
