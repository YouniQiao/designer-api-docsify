# createBundleContext（系统接口）

## 导入模块

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createBundleContext

```TypeScript
export function createBundleContext(context: Context, bundleName: string): Promise<Context>
```

根据入参Context创建相应应用的Context。使用Promise异步回调。

> **说明：**&gt;
> 从API version 18开始，Context支持获取当前应用的进程名
> [processName](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#context)。
> createBundleContext创建的Context中的processName属性与入参Context中的processName属性一致，其他属性根据入参Context和bundleName获得相应
> 的属性值。

**起始版本：** 12

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
