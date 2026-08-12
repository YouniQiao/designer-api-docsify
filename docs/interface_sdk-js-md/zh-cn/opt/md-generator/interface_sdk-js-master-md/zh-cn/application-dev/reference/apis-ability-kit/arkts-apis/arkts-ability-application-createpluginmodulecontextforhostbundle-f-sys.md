# createPluginModuleContextForHostBundle（系统接口）

## createPluginModuleContextForHostBundle

```TypeScript
export function createPluginModuleContextForHostBundle(context: Context, pluginBundleName: string, pluginModuleName: string,
    hostBundleName: string): Promise<Context>
```

根据入参Context、插件包名和插件模块名和应用包名，创建对应插件的Context，用于获取插件的基本信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-application-export function createPluginModuleContextForHostBundle(context: Context, pluginBundleName: string, pluginModuleName: string,    hostBundleName: string): Promise<Context>--><!--Device-application-export function createPluginModuleContextForHostBundle(context: Context, pluginBundleName: string, pluginModuleName: string,    hostBundleName: string): Promise<Context>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | 是 |
| pluginModuleName | string | 是 |
| hostBundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createPluginModuleContextForHostBundle(this.context, 'com.example.pluginBundleName', 'pluginModuleName', 'com.example.hostBundleName')
        .then((data: common.Context) => {
          moduleContext = data;
          console.info('createPluginModuleContextForHostBundle success!');
        })
        .catch((error: BusinessError) => {
          console.error(`createPluginModuleContextForHostBundle failed, error.code: ${error.code}, error.message: ${error.message}`);
        });
    } catch (error: BusinessError) {
      console.error(`createPluginModuleContextForHostBundle failed, error.code: ${error.code}, error.message: ${error.message}`);
    }
  }
}
```
