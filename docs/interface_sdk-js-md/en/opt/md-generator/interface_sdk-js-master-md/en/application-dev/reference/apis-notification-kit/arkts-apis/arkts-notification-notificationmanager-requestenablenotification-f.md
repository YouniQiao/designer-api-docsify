# requestEnableNotification

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## requestEnableNotification

```TypeScript
function requestEnableNotification(callback: AsyncCallback<void>): void
```

Requests notification to be enabled for this application. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [requestEnableNotification](#requestEnableNotification)

<!--Device-notificationManager-function requestEnableNotification(callback: AsyncCallback<void>): void--><!--Device-notificationManager-function requestEnableNotification(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600013-notification-popup-window-displayed) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600004-notification-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let requestEnableNotificationCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`requestEnableNotification success`);
  }
};
notificationManager.requestEnableNotification(requestEnableNotificationCallback);
```


## requestEnableNotification

```TypeScript
function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void
```

Requests notification to be enabled for this application. You can call this API to display a dialog box prompting the user to enable notification for your application before publishing a notification. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - This API can be called only after the application UI is loaded (that is,
> [loadContent](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md#loadContent) is
> successfully called).
> 
> - When an application uses **requestEnableNotification()** to display a dialog box for notification authorization
> and the user rejects the authorization, the application cannot use this API to open the dialog box again. However
> , it can call [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md#openNotificationSettingsWithResult)
> to open the notification management dialog box.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[isNotificationEnabled](notificationManager.isNotificationEnabled(callback: AsyncCallback<boolean>): void) checks whether

[openNotificationSettingsWithResult](notificationManager.openNotificationSettingsWithResult(context: UIAbilityContext): 
   *     Promise<NotificationSetting>) Opens the notification settings page of the application, which is presented in a semi-modal

[openNotificationSettings](notificationManager.openNotificationSettings(context: UIAbilityContext): Promise<void>) opens the

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600013-notification-popup-window-displayed) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600004-notification-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      let requestEnableNotificationCallback = (err: BusinessError): void => {
        if (err) {
          hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
        } else {
          hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
        }
      };
      notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
    });
  }
}
```


## requestEnableNotification

```TypeScript
function requestEnableNotification(): Promise<void>
```

Requests notification to be enabled for this application. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [requestEnableNotification](#requestEnableNotification)

<!--Device-notificationManager-function requestEnableNotification(): Promise<void>--><!--Device-notificationManager-function requestEnableNotification(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600013-notification-popup-window-displayed) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600004-notification-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.requestEnableNotification().then(() => {
  console.info(`requestEnableNotification success`);
}).catch((err: BusinessError) => {
  console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
});
```


## requestEnableNotification

```TypeScript
function requestEnableNotification(context: UIAbilityContext): Promise<void>
```

Requests notification to be enabled for this application. You can call this API to display a dialog box prompting the user to enable notification for your application before publishing a notification. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API can be called only after the application UI is loaded (that is,
> [loadContent](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md#loadContent) is
> successfully called).
> 
> - When an application uses **requestEnableNotification()** to display a dialog box for notification authorization
> and the user rejects the authorization, the application cannot use this API to open the dialog box again. However
> , it can call [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md#openNotificationSettingsWithResult)
> to open the notification management dialog box.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function requestEnableNotification(context: UIAbilityContext): Promise<void>--><!--Device-notificationManager-function requestEnableNotification(context: UIAbilityContext): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[isNotificationEnabled](notificationManager.isNotificationEnabled(callback: AsyncCallback<boolean>): void) checks whether

[openNotificationSettingsWithResult](notificationManager.openNotificationSettingsWithResult(context: UIAbilityContext): 
   *     Promise<NotificationSetting>) Opens the notification settings page of the application, which is presented in a semi-modal

[openNotificationSettings](notificationManager.openNotificationSettings(context: UIAbilityContext): Promise<void>) opens the

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600013-notification-popup-window-displayed) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600004-notification-disabled) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      notificationManager.requestEnableNotification(this.context).then(() => {
        hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
      });
    });
  }
}
```
