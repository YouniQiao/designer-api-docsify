# queryAbilityInfoSync（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## queryAbilityInfoSync

```TypeScript
function queryAbilityInfoSync(want: Want, abilityFlags: number, userId?: number): Array<AbilityInfo>
```

以同步方法根据给定的want、abilityFlags和userId获取一个或多个AbilityInfo。获取调用方自身的信息时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| abilityFlags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;AbilityInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |
