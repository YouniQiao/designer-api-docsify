# @ohos.app.ability.UIExtensionContentSession

UIExtensionContentSession is the UI operation class for the
 [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md). It provides control over page
 loading and allows configuration of the window privacy mode of the host application (application that starts the
 UIExtensionAbility). When the host application starts a specific UIExtensionAbility, the system creates a
 UIExtensionContentSession object and passes it back via the
 [onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate) callback. Each
 UIExtensionAbility corresponds to one UIExtensionContentSession object, and these objects operate independently
 without interfering with each other.


## Summary

### Classes

| Name | Description |
| --- | --- |
| [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | UIExtensionContentSession is the UI operation class for the UIExtensionAbility. It provides control over page loading and allows configuration of the window privacy mode of the host application. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c-sys.md) | UIExtensionContentSession is the UI operation class for the UIExtensionAbility. It provides control over page loading and allows configuration of the window privacy mode of the host application. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [OnReceiveDataCallback](arkts-ability-onreceivedatacallback-t-sys.md) | Sets the callback for the ui extension to receive data from an ui extension component. |
| [OnReceiveDataForResultCallback](arkts-ability-onreceivedataforresultcallback-t-sys.md) | Sets the callback with return value for the ui extension to receive data from an ui extension component. |
<!--DelEnd-->

