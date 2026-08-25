# createPluginModuleContextForHostBundle（系统接口）

## 导入模块

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createPluginModuleContextForHostBundle

```TypeScript
export function createPluginModuleContextForHostBundle(context: Context, pluginBundleName: string, pluginModuleName: string,
    hostBundleName: string): Promise<Context>
```

根据入参Context、插件包名、插件模块名和安装插件的应用包名，创建对应插件的Context，用于获取插件的基本信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | 是 |
| pluginModuleName | string | 是 |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
