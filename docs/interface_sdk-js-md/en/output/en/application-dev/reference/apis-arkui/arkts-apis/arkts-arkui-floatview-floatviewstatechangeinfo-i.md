# FloatViewStateChangeInfo

Provides the state change information of the float view.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-floatView-interface FloatViewStateChangeInfo--><!--Device-floatView-interface FloatViewStateChangeInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## state

```TypeScript
state: FloatViewState
```

State of the float view.

**Type:** FloatViewState

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewStateChangeInfo-state: FloatViewState--><!--Device-FloatViewStateChangeInfo-state: FloatViewState-End-->

**System capability:** SystemCapability.Window.SessionManager

## stopReason

```TypeScript
stopReason: string
```

Reason why the float view stops. This parameter is valid only when **state** is set to **FloatViewState.STOPPED**. In other states, this parameter is an empty string by default. The stop reasons and their meanings are as follows: **"APP\_STOP"**: The application proactively stops the float view. **"STOP\_IN\_SIDEBAR"**: The float view is closed in the sidebar. **"TITLE\_BAR\_STOP\_CLICK"**: The float view is closed by clicking the close button on the title bar. **"DUMPSTER\_STOP"**: The float view is dragged to the trash can. **"REPLACE\_STOP"**: The float view is occupied by another float view. **"FLOATING\_BALL\_STOP"**: The float view stops when the bound floating ball stops. **"MAIN\_WINDOW\_DESTROY\_STOP"**: The float view stops after the main window associated with the context is destroyed.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewStateChangeInfo-stopReason: string--><!--Device-FloatViewStateChangeInfo-stopReason: string-End-->

**System capability:** SystemCapability.Window.SessionManager

