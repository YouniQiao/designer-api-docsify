# WebNativeMessagingExtensionContext

WebNativeMessagingExtensionContext是Web原生消息扩展（ [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md)）的运行上下文，继承自ExtensionContext，为 扩展Ability提供生命周期管理、Ability启动以及原生消息连接控制能力。开发者可在继承WebNativeMessagingExtensionAbility的扩展中通过`this.context`获取该上下文，进而调用 [startAbility](#startability)启动其他Ability、调用 [startAbilityForResult](#startabilityforresult)启动UIAbility并接收返回结果、调用 [terminateSelf](#terminateself)结束当前扩展，或调用 [stopNativeConnection](#stopnativeconnection)停止指定的Web原生消息连接。

> **说明:**&gt;
> 本模块接口仅可在Stage模型下使用。

**继承/实现关系：** WebNativeMessagingExtensionContext extends ExtensionContext

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

使用Promise异步回调启动Ability。如需获取启动的UIAbility退出时的返回结果，可以使用 [startAbilityForResult](#startabilityforresult)。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000071](../../apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000072](../../apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000073](../../apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000076](../../apis-ability-kit/errorcode-ability.md#16000076-指定的app_instance_key不存在) |
| [16000077](../../apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../apis-ability-kit/errorcode-ability.md#16000079-不支持指定app_instance_key) |
| [16000080](../../apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
      bundleName: 'com.example.mybundle',
      abilityName: 'MainAbility'
    };
    try {
      const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
      context.startAbility(abilityWant).then(() => {
        console.info('Ability started successfully');
      }).catch((err: BusinessError) => {
        console.error(`Failed to start ability. Code: ${err.code},
          Message: ${err.message}`);
      });
    } catch (err) {
      console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
      Message: ${(err as BusinessError).message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { ConnectionInfo } from '@ohos.web.WebNativeMessagingExtensionAbility'
import WebNativeMessagingExtensionAbility from "@ohos.web.WebNativeMessagingExtensionAbility"
import Want from '@ohos.app.ability.Want'
import { BusinessError } from '@ohos.base'

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
    bundleName: 'com.example.mybundle',
    abilityName: 'MainAbility'
    };
    try {
        const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
        context.startAbility(abilityWant);
        console.info('Ability started successfully');
    } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(`Failed to start ability. Code: ${code}, Message: ${message}`);
    }
  }
}
```

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

启动一个UIAbility，使用Promise异步回调接收被拉起的UIAbility退出时的返回结果。 UIAbility被启动后，有如下情况:  
- 正常情况下可通过调用 [terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止并且返回结果给调用方。 - 异常情况下比如销毁UIAbility会返回异常信息给调用方，异常信息中resultCode为-1。 - 只支持拉起自己应用的UIAbility。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000071](../../apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000072](../../apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000073](../../apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000076](../../apis-ability-kit/errorcode-ability.md#16000076-指定的app_instance_key不存在) |
| [16000077](../../apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../apis-ability-kit/errorcode-ability.md#16000079-不支持指定app_instance_key) |
| [16000080](../../apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
      bundleName: 'com.example.mybundle', // 请开发者替换为实际的 bundleName
      abilityName: 'MainAbility' // 请开发者替换为实际的 abilityName
    };
    try {
      const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
      context.startAbilityForResult(abilityWant).then((result: common.AbilityResult) => {
        console.info(`Ability started successfully, result code: ${result.resultCode}`);
        if (result.want) {
          console.info(`Result data: ${JSON.stringify(result.want)}`);
        }
      }).catch((err: BusinessError) => {
        console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
        Message: ${(err as BusinessError).message}`);
      });
    } catch (err) {
      console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
      Message: ${(err as BusinessError).message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import WebNativeMessagingExtensionAbility from '@ohos.web.WebNativeMessagingExtensionAbility'
import { ConnectionInfo } from '@ohos.web.WebNativeMessagingExtensionAbility';
import { Want, common } from '@kit.AbilityKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
      bundleName: 'com.example.mybundle', // 请开发者替换为实际的 bundleName
      abilityName: 'MainAbility' // 请开发者替换为实际的 abilityName
    };
    try {
      const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
      context.startAbilityForResult(abilityWant).then((result: common.AbilityResult) => {
        console.info(`Ability started successfully, result code: ${result.resultCode}`);
        if (result.want) {
          console.info(`Result data: ${JSON.stringify(result.want)}`);
        }
      }).catch((err: Error) => {
        console.error(`Failed to start ability. Code: ${err.name}, Message: ${err.message}`);
      });
    } catch (err) {
      console.error(`Failed to start ability. Code: ${(err as Error).name}, Message: ${(err as Error).message}`);
    }
  }
}
```

## stopNativeConnection

```TypeScript
stopNativeConnection(connectionId: number): Promise<void>
```

停止指定的本地连接。使用Promise异步回调。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connectionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const CONNECTION_ID = 12345; // 实际的连接 ID
    try {
        const context = this.context;// 获取 WebNativeMessagingExtensionContext 实例
        context.stopNativeConnection(CONNECTION_ID).then(() => {
          console.info('Native connection stopped successfully');
        }).catch((err: BusinessError) => {
          console.error(`Failed to stop native connection. Code: ${err.code},
          Message: ${err.message}`);
        })
    } catch (err) {
        console.error(`Failed to stop native connection. Code: ${(err as BusinessError).code},
        Message: ${(err as BusinessError).message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { ConnectionInfo } from '@ohos.web.WebNativeMessagingExtensionAbility'
import WebNativeMessagingExtensionAbility from "@ohos.web.WebNativeMessagingExtensionAbility"
import { BusinessError } from '@ohos.base'

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const CONNECTION_ID = 12345; // 实际的连接 ID
    try {
        const context = this.context;// 获取 WebNativeMessagingExtensionContext 实例
        context.stopNativeConnection(CONNECTION_ID);
        console.info('Native connection stopped successfully');
    } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(`Failed to stop native connection. Code: ${code}, Message: ${message}`);
    }
  }
}
```

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁当前Web原生消息扩展。该方法返回一个Promise对象用于异步处理，调用此方法会自动停止所有Web原生消息连接，无需再调用stopNativeConnection。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    try {
        const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
        context.terminateSelf().then(() => {
          console.info('Extension terminated successfully');
        }).catch((err: BusinessError) => {
          console.error(`Failed to terminate extension. Code: ${err.code},
          Message: ${err.message}`);
        });       
    } catch (err) {
        console.error(`Failed to terminate extension. Code: ${(err as BusinessError).code},
        Message: ${(err as BusinessError).message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { ConnectionInfo } from '@ohos.web.WebNativeMessagingExtensionAbility'
import WebNativeMessagingExtensionAbility from "@ohos.web.WebNativeMessagingExtensionAbility"
import { BusinessError } from '@ohos.base'

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    try {
        const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
        context.terminateSelf();
        console.info('Extension terminated successfully');
    } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(`Failed to start ability. Code: ${code}, Message: ${message}`);
    }
  }
}
```
