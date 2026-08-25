# getShortcutInfoByAppIndex（系统接口）

## 导入模块

```TypeScript
import { launcherBundleManager } from 'kits/@kit.AbilityKit';
```

## getShortcutInfoByAppIndex

```TypeScript
function getShortcutInfoByAppIndex(bundleName: string, appIndex: number): Array<ShortcutInfo>
```

查询当前用户下指定分身应用的快捷方式信息ShortcutInfo。调用方获取自己的信息时不需要权限。

**起始版本：** 20

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |

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
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
