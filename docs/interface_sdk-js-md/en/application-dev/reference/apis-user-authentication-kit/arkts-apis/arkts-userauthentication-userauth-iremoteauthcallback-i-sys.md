# IRemoteAuthCallback (System API)

Defines the remote authentication callback API. This API is used in remote authentication scenarios and provides the callback capabilities for obtaining remote authentication widget parameters and returning authentication results.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-userAuth-interface IRemoteAuthCallback--><!--Device-userAuth-interface IRemoteAuthCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## onGetRemoteAuthWidgetParam

```TypeScript
onGetRemoteAuthWidgetParam: WidgetParamCallback
```

Callback for obtaining remote authentication widget parameters. When a remote device initiates an authentication request, the system invokes this callback to obtain the authentication widget configuration parameters.

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

Callback for returning remote authentication results. After the remote authentication is complete, the system invokes this callback to return the authentication result to the initiator.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IRemoteAuthCallback-onRemoteAuthResult: ResultCallback--><!--Device-IRemoteAuthCallback-onRemoteAuthResult: ResultCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

