# IRemoteAuthCallback (System API)

远程认证回调接口。该接口用于远程认证场景，提供获取远程认证页面参数和返回认证结果的回调能力。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-userAuth-interface IRemoteAuthCallback--><!--Device-userAuth-interface IRemoteAuthCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## onGetRemoteAuthWidgetParam

```TypeScript
onGetRemoteAuthWidgetParam: WidgetParamCallback
```

获取远程认证页面参数的回调函数。在远程设备发起认证请求时，系统会调用此回调获取认证界面配置参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IRemoteAuthCallback-onGetRemoteAuthWidgetParam: WidgetParamCallback--><!--Device-IRemoteAuthCallback-onGetRemoteAuthWidgetParam: WidgetParamCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## onRemoteAuthResult

```TypeScript
onRemoteAuthResult: ResultCallback
```

返回远程认证结果的回调函数。在远程认证完成后，系统会调用此回调将认证结果返回给发起方。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IRemoteAuthCallback-onRemoteAuthResult: ResultCallback--><!--Device-IRemoteAuthCallback-onRemoteAuthResult: ResultCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

