# AutoFillExtensionContext（系统接口）

```TypeScript
declare class AutoFillExtensionContext extends ExtensionContext
```

AutoFillExtensionContext模块是AutoFillExtensionAbility的上下文环境，继承自[ExtensionContext](arkts-ability-extensioncontext-c.md)。

**继承/实现关系：** AutoFillExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**起始版本：** 11

<!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前AutoFillExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，由系统提供，通常用于提供指定场景的后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

> **说明：** 
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AutoFillExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-AutoFillExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 | 连接ServiceExtensionAbility的Want信息，包括Ability名称、Bundle名称等。 |
| options | [ConnectOptions](arkts-ability-connectoptions-i.md) | 是 | 回调函数，返回服务连接成功、连接失败、断开的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，客户端可以通过[disconnectServiceExtensionAbility](#disconnectserviceextensionability)传入该连接id来断开连接。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) | The specified ability does not exist. |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) | Incorrect ability type. |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) | Cannot start an invisible component. |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) | The specified process does not have the permission. |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) | Cross-user operations are not allowed. |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) | The crowdtesting application expires. |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) | The context does not exist. |
| [16000012](../errorcode-ability.md#16000012-应用被管控) | The application is controlled. |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) | The application is controlled by EDM. |
| [16000050](../errorcode-ability.md#16000050-内部错误) | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) | The ability is not on the top of the UI. |
| [16000055](../errorcode-ability.md#16000055-免安装超时) | Installation-free timed out. |
| [16000070](../errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) | The extension cannot start the service. |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，由系统提供，通常用于提供指定场景的后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AutoFillExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-AutoFillExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识Id，即[connectServiceExtensionAbility](#connectserviceextensionability)返回的connectionId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) | The context does not exist. |
| [16000050](../errorcode-ability.md#16000050-内部错误) | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |

## reloadInModal

```TypeScript
reloadInModal(customData: CustomData): Promise<void>
```

重新拉起模态页面。使用Promise异步回调。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>--><!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customData | [CustomData](arkts-ability-customdata-i-sys.md) | 是 | 拉起模态页面时的自定义信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-函数参数数量或参数类型不匹配) | If the input parameter is not valid parameter. |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) | The context does not exist. |
| [16000050](../errorcode-ability.md#16000050-内部错误) | Internal error. |

<!--Del-->
**示例**

通过点击账号密码输入框触发自动填充服务时，在[AutoFillExtensionAbility](arkts-ability-app-ability-autofillextensionability-autofillextensionability-c-sys.md)的onFillRequest生命周期中拉起账号选择界面。

当点击账号选择界面选择任意账号时，调用reloadInModal接口再次触发自动填充服务，在AutoFillExtensionAbility的onFillRequest生命周期中拉起模态页面。

```TypeScript
// AutoFillAbility.ts
import { AutoFillExtensionAbility, autoFillManager, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class AutoFillAbility extends AutoFillExtensionAbility {
  // ...
  onFillRequest(session: UIExtensionContentSession,
    request: autoFillManager.FillRequest,
    callback: autoFillManager.FillRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'autofill onFillRequest');
    try {
      // 创建LocalStorage并存储自动填充所需的数据
      let storage_fill: LocalStorage = new LocalStorage(
        {
          'session': session,
          'message': "AutoFill Page",
          'fillCallback': callback,
          'viewData': request.viewData,
          'autoFillExtensionContext': this.context,
          'customData': request.customData
        } as Record<string, Object>);
      if (request.customData == undefined) {
        // 加载自动填充处理界面
        session.loadContent('pages/AccountPage', storage_fill);
      } else {
        // 拉起模态页面
        session.loadContent('pages/ReloadInModal', storage_fill);
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'autofill failed to load content');
    }
  }
}
```

当点击账号选择界面选择任意账号时，调用reloadInModal接口。

```TypeScript
// AccountPage.ets
import { autoFillManager, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct AccountPage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  viewData: autoFillManager.ViewData | undefined = this.storage?.get<autoFillManager.ViewData>('viewData');
  context: common.AutoFillExtensionContext | undefined = this.storage?.get<common.AutoFillExtensionContext>('autoFillExtensionContext');


  build() {
    Row() {
      Column() {
        List({ space: 10, initialIndex: 0 }) {
          ListItem() {
            Text('HelloWorld789456')
              .width('100%')
              .height(40)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(5)
          }
          .onClick(() => {
            if (this.viewData != undefined) {
              if (this.context != undefined) {
                // 调用reloadInModal接口重新触发自动填充，传递自定义数据用于模态页面
                this.context.reloadInModal({ data: { viewData: 20, text: 'HelloWorld789456' } }).then(() => {
                  console.info('reloadInModal successfully.')
                }).catch((err: BusinessError) => {
                  console.error(`reloadInModal failed. Code: ${err.code}, message: ${err.message}`);
                })
              }
            }
          });
        }
        // ...
      }
      .width('100%')
      .shadow(ShadowStyle.OUTER_FLOATING_SM)
    }
    .height('100%')
    .shadow(ShadowStyle.OUTER_FLOATING_SM)
  }
}
```

<!--DelEnd-->
