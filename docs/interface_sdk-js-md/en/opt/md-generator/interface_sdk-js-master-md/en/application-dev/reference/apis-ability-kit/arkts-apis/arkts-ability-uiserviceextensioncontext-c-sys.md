# UIServiceExtensionContext (System API)

The UIServiceExtensionContext module provides the context environment for a  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#UIServiceExtensionAbility). It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md#ExtensionContext).

UIServiceExtensionContext provides access to a  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#UIServiceExtensionAbility) and APIs for operating the ability, for example, starting, terminating, connecting, and disconnecting ability.

> **NOTE：**
> 
> - The APIs of this module must be used on the main thread, but not on child threads such as Worker and TaskPool.

**Inheritance/Implementation:** UIServiceExtensionContext extends [ExtensionContext](ExtensionContext)

**Since:** 14

<!--Device-unnamed-declare class UIServiceExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIServiceExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

Connects to a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility) and returns the connection ID.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIServiceExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { common, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[Page_ServiceExtensionAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

let connectionId: number;
let want: Want = {
  deviceId: '',
  bundleName: 'com.samples.stagemodelabilitydevelop',
  abilityName: 'ServiceExtAbility'
};

let options: common.ConnectOptions = {
  onConnect(elementName, remote: rpc.IRemoteObject): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
  },
  onDisconnect(elementName): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
  },
  onFailed(code: number): void {
    hilog.info(DOMAIN_NUMBER, TAG, `onFailed callback, ${code}`);
  }
};

@Entry
@Component
struct Page_UIServiceExtensionAbility {
  build() {
    Column() {
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
          }
          .onClick(() => {
            let context: common.UIServiceExtensionContext =
              this.getUIContext().getHostContext() as common.UIServiceExtensionContext;
            // The ID returned after the connection is set up must be saved. The ID will be used for disconnection.
            connectionId = context.connectServiceExtensionAbility(want, options);
            // The background service is connected.
            this.getUIContext().getPromptAction().showToast({
              message: 'SuccessfullyConnectBackendService'
            });
            // connectionId = context.connectAbility(want, options);
            hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
          })
        }
      }
    }
  }
}
```

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connectionId: number): Promise<void>
```

Disconnects from a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility). This API is opposite to [connectServiceExtensionAbility](#connectServiceExtensionAbility). This API uses a promise to return the result.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-disconnectServiceExtensionAbility(connectionId: long): Promise<void>--><!--Device-UIServiceExtensionContext-disconnectServiceExtensionAbility(connectionId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connectionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[Page_ServiceExtensionAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

let connectionId: number;

@Entry
@Component
struct Page_UIServiceExtensionAbility {
  build() {
    Column() {
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
          }
          .onClick(() => {
            let context: common.UIServiceExtensionContext =
              this.getUIContext().getHostContext() as common.UIServiceExtensionContext;
            // connectionId is returned when connectServiceExtensionAbility is called and needs to be manually maintained.
            context.disconnectServiceExtensionAbility(connectionId).then(() => {
              hilog.info(DOMAIN_NUMBER, TAG, 'disconnectServiceExtensionAbility success');
              // The background service is disconnected.
              this.getUIContext().getPromptAction().showToast({
                message: 'SuccessfullyDisconnectBackendService'
              });
            }).catch((err: BusinessError) => {
              hilog.error(DOMAIN_NUMBER, TAG,
                `disconnectServiceExtensionAbility failed, err code: ${err.code}, err msg: ${err.message}`);
            });
          })
        }
      }
    }
  }
}
```

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts an ability. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { UIServiceExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class UIEntryAbility extends UIServiceExtensionAbility {
  onCreate() {
    let want: Want = {
      bundleName: 'com.example.myapp',
      abilityName: 'MyAbility'
    };
    let options: StartOptions = {
      windowMode: 0,
    };

    try {
      this.context.startAbility(want, options)
        .then((data: void) => {
          // Carry out normal service processing.
          console.info('startAbility succeed');
        })
        .catch((error: BusinessError) => {
          // Process service logic errors.
          console.error(`startAbility failed, error.code: ${error.code}, error.message: ${error.message}`);
        });
    } catch (paramError) {
      // Process input parameter errors.
      console.error(`error.code: ${paramError.code}, error.message: ${paramError.message}`);
    }
  }
}
```

## startAbilityByType

```TypeScript
startAbilityByType(type: string, wantParam: Record<string, Object>,
    abilityStartCallback: AbilityStartCallback): Promise<void>
```

Starts a [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) or  
[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility) based on the type of the target ability. This API can be called only by applications running in the foreground. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>--><!--Device-UIServiceExtensionContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| wantParam | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |
| abilityStartCallback | [AbilityStartCallback](arkts-ability-abilitystartcallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[Extension_Sub] ';

@Entry
@Component
struct SubIndex {
  build() {
    Row() {
      Column() {
        Button("startAbilityByType")
          .fontSize(10)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIServiceExtensionContext;
            let startWant: Record<string, Object> = {
              'sceneType': 1,
              'email': [encodeURI('xxx@example.com'),
                encodeURI('xxx@example.com')], // Email address of the recipient. Multiple values are separated by commas (,). The array content is URL-encoded using the **encodeURI()** method.
              'cc': [encodeURI('xxx@example.com'),
                encodeURI('xxx@example.com')], // Email address of the CC recipient. Multiple values are separated by commas (,). The array content is URL-encoded using the **encodeURI()** method.
              'bcc': [encodeURI('xxx@example.com'),
                encodeURI('xxx@example.com')], // Email address of the BCC recipient. Multiple values are separated by commas (,). The array content is URL-encoded using the **encodeURI()** method.
              'subject': encodeURI('Email subject'), // Email subject. The content is URL encoded using encodeURI().
              'body': encodeURI('Email body'), // Email body. The content is URL encoded using encodeURI().
              'ability.params.stream': [encodeURI ('attachment uri1'),
                encodeURI ('attachment uri2') ], // Attachment URI. Multiple values are separated by commas (,). The array content is URL-encoded using the encodeURI() method.
              'ability.want.params.uriPermissionFlag': 1
            };
            let abilityStartCallback: common.AbilityStartCallback = {
              onError: (code: number, name: string, message: string) => {
                console.error(TAG + `code: ${code}  name:${name}  message:${message}`);
              }
            };
            try {
              // Start a UIAbility or UIExtensionAbility based on the type of the target ability.
              context.startAbilityByType("mail", startWant, abilityStartCallback)
                .then(() => {
                  console.info(TAG + `Succeeded in windows starting ability`);
                }).catch((err: BusinessError) => {
                console.error(TAG +
                  `Failed to windows starting ability, Code is ${err.code}, message is ${err.message}.`);
              })
            } catch (err) {
              let code = (err as BusinessError).code;
              let msg = (err as BusinessError).message;
              console.error(TAG + `Failed to windows starting ability, Code is ${code}, message is ${msg}.`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Terminates this  
[UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#UIServiceExtensionAbility). This API uses a promise to return the result.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionContext-terminateSelf(): Promise<void>--><!--Device-UIServiceExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import { UIServiceExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class UIEntryAbility extends UIServiceExtensionAbility {
  onCreate() {
    this.context.terminateSelf().then(() => {
      // Carry out normal service processing.
      console.info('terminateSelf succeed');
    }).catch((error: BusinessError) => {
      // Process service logic errors.
      console.error(`terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
    });
  }
}
```
