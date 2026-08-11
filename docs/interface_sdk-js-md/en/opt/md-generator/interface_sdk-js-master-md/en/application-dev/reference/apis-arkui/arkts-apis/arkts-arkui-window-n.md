# window

Window manager.

**Since:** 6

<!--Device-unnamed-declare namespace window--><!--Device-unnamed-declare namespace window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createWindow](arkts-arkui-window-createwindow-f.md#createwindow) |
| [createWindow](arkts-arkui-window-createwindow-f.md#createwindow-1) |
| [create](arkts-arkui-window-create-f.md#create) |
| [create](arkts-arkui-window-create-f.md#create-1) |
| [create](arkts-arkui-window-create-f.md#create-2) |
| [create](arkts-arkui-window-create-f.md#create-3) |
| [find](arkts-arkui-window-find-f.md#find) |
| [find](arkts-arkui-window-find-f.md#find-1) |
| [findWindow](arkts-arkui-window-findwindow-f.md#findwindow) |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#gettopwindow) |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#gettopwindow-1) |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#gettopwindow-2) |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#gettopwindow-3) |
| [getLastWindow](arkts-arkui-window-getlastwindow-f.md#getlastwindow) |
| [getLastWindow](arkts-arkui-window-getlastwindow-f.md#getlastwindow-1) |
| [shiftAppWindowFocus](arkts-arkui-window-shiftappwindowfocus-f.md#shiftappwindowfocus) |
| [shiftAppWindowPointerEvent](arkts-arkui-window-shiftappwindowpointerevent-f.md#shiftappwindowpointerevent) |
| [shiftAppWindowTouchEvent](arkts-arkui-window-shiftappwindowtouchevent-f.md#shiftappwindowtouchevent) |
| [getVisibleWindowInfo](arkts-arkui-window-getvisiblewindowinfo-f.md#getvisiblewindowinfo) |
| [getWindowsByCoordinate](arkts-arkui-window-getwindowsbycoordinate-f.md#getwindowsbycoordinate) |
| [getAllWindowLayoutInfo](arkts-arkui-window-getallwindowlayoutinfo-f.md#getallwindowlayoutinfo) |
| [getAllWindowLayoutInfo](arkts-arkui-window-getallwindowlayoutinfo-f.md#getallwindowlayoutinfo-1) |
| [getGlobalWindowMode](arkts-arkui-window-getglobalwindowmode-f.md#getglobalwindowmode) |
| [onApplicationFocusStateChange](arkts-arkui-window-onapplicationfocusstatechange-f.md#onapplicationfocusstatechange) |
| [offApplicationFocusStateChange](arkts-arkui-window-offapplicationfocusstatechange-f.md#offapplicationfocusstatechange) |
| [setStartWindowBackgroundColor](arkts-arkui-window-setstartwindowbackgroundcolor-f.md#setstartwindowbackgroundcolor) |
| [setWatermarkImageForAppWindows](arkts-arkui-window-setwatermarkimageforappwindows-f.md#setwatermarkimageforappwindows) |
| [getAllMainWindowInfo](arkts-arkui-window-getallmainwindowinfo-f.md#getallmainwindowinfo) |
| [getMainWindowSnapshot](arkts-arkui-window-getmainwindowsnapshot-f.md#getmainwindowsnapshot) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createSubWindowAndBindParent](arkts-arkui-window-createsubwindowandbindparent-f-sys.md#createsubwindowandbindparent) |
| [minimizeAll](arkts-arkui-window-minimizeall-f-sys.md#minimizeall) |
| [minimizeAll](arkts-arkui-window-minimizeall-f-sys.md#minimizeall-1) |
| [minimizeAllWithExclusion](arkts-arkui-window-minimizeallwithexclusion-f-sys.md#minimizeallwithexclusion) |
| [toggleShownStateForAllAppWindows](arkts-arkui-window-toggleshownstateforallappwindows-f-sys.md#toggleshownstateforallappwindows) |
| [toggleShownStateForAllAppWindows](arkts-arkui-window-toggleshownstateforallappwindows-f-sys.md#toggleshownstateforallappwindows-1) |
| [setWindowLayoutMode](arkts-arkui-window-setwindowlayoutmode-f-sys.md#setwindowlayoutmode) |
| [setWindowLayoutMode](arkts-arkui-window-setwindowlayoutmode-f-sys.md#setwindowlayoutmode-1) |
| [setGestureNavigationEnabled](arkts-arkui-window-setgesturenavigationenabled-f-sys.md#setgesturenavigationenabled) |
| [setGestureNavigationEnabled](arkts-arkui-window-setgesturenavigationenabled-f-sys.md#setgesturenavigationenabled-1) |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setwatermarkimage) |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setwatermarkimage-1) |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setwatermarkimage-2) |
| [setSpecificSystemWindowZIndex](arkts-arkui-window-setspecificsystemwindowzindex-f-sys.md#setspecificsystemwindowzindex) |
| [getTopNavDestinationName](arkts-arkui-window-gettopnavdestinationname-f-sys.md#gettopnavdestinationname) |
| [getSnapshot](arkts-arkui-window-getsnapshot-f-sys.md#getsnapshot) |
| [on](arkts-arkui-window-on-f-sys.md#on) |
| [off](arkts-arkui-window-off-f-sys.md#off) |
| [on](arkts-arkui-window-on-f-sys.md#on-1) |
| [off](arkts-arkui-window-off-f-sys.md#off-1) |
| [on](arkts-arkui-window-on-f-sys.md#on-2) |
| [off](arkts-arkui-window-off-f-sys.md#off-2) |
| [notifyScreenshotEvent](arkts-arkui-window-notifyscreenshotevent-f-sys.md#notifyscreenshotevent) |
| [moveMainWindowToTargetDisplay](arkts-arkui-window-movemainwindowtotargetdisplay-f-sys.md#movemainwindowtotargetdisplay) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) |
| [StatusBarProperty](arkts-arkui-window-statusbarproperty-i.md) |
| [SystemBarStyle](arkts-arkui-window-systembarstyle-i.md) |
| [FrameMetrics](arkts-arkui-window-framemetrics-i.md) |
| [Rect](arkts-arkui-window-rect-i.md) |
| [RectInVP](arkts-arkui-window-rectinvp-i.md) |
| [Position](arkts-arkui-window-position-i.md) |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) |
| [UIEnvAvoidAreaVP](arkts-arkui-window-uienvavoidareavp-i.md) |
| [Size](arkts-arkui-window-size-i.md) |
| [SizeInVP](arkts-arkui-window-sizeinvp-i.md) |
| [WindowInfo](arkts-arkui-window-windowinfo-i.md) |
| [WindowDensityInfo](arkts-arkui-window-windowdensityinfo-i.md) |
| [WindowProperties](arkts-arkui-window-windowproperties-i.md) |
| [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) |
| [Configuration](arkts-arkui-window-configuration-i.md) |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) |
| [TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md) |
| [RectChangeOptions](arkts-arkui-window-rectchangeoptions-i.md) |
| [AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md) |
| [UIEnvWindowAvoidAreaInfoPX](arkts-arkui-window-uienvwindowavoidareainfopx-i.md) |
| [UIEnvWindowAvoidAreaInfoVP](arkts-arkui-window-uienvwindowavoidareainfovp-i.md) |
| [MainWindowInfo](arkts-arkui-window-mainwindowinfo-i.md) |
| [WindowSnapshotConfiguration](arkts-arkui-window-windowsnapshotconfiguration-i.md) |
| [OrientationResult](arkts-arkui-window-orientationresult-i.md) |
| [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md) |
| [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) |
| [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md) |
| [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) |
| [MaximizeOptions](arkts-arkui-window-maximizeoptions-i.md) |
| [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) |
| [StartAnimationParams](arkts-arkui-window-startanimationparams-i.md) |
| [WindowCreateParams](arkts-arkui-window-windowcreateparams-i.md) |
| [WindowSnapshotAnimationConfig](arkts-arkui-window-windowsnapshotanimationconfig-i.md) |
| [KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md) |
| [KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md) |
| [Window](arkts-arkui-window-window-i.md) |
| [ShowWindowOptions](arkts-arkui-window-showwindowoptions-i.md) |
| [SubWindowOptions](arkts-arkui-window-subwindowoptions-i.md) |
| [WindowStage](arkts-arkui-window-windowstage-i.md) |
| [WindowLayoutInfo](arkts-arkui-window-windowlayoutinfo-i.md) |
| [WindowInfoOptions](arkts-arkui-window-windowinfooptions-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SystemBarRegionTint](arkts-arkui-window-systembarregiontint-i-sys.md) |
| [SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md) |
| [WindowAnchorInfo](arkts-arkui-window-windowanchorinfo-i-sys.md) |
| [SubWindowAttachOptions](arkts-arkui-window-subwindowattachoptions-i-sys.md) |
| [ScaleOptions](arkts-arkui-window-scaleoptions-i-sys.md) |
| [RotateOptions](arkts-arkui-window-rotateoptions-i-sys.md) |
| [TranslateOptions](arkts-arkui-window-translateoptions-i-sys.md) |
| [TransitionContext](arkts-arkui-window-transitioncontext-i-sys.md) |
| [TransitionController](arkts-arkui-window-transitioncontroller-i-sys.md) |
| [Configuration](arkts-arkui-window-configuration-i-sys.md) |
| [StartMovingOptions](arkts-arkui-window-startmovingoptions-i-sys.md) |
| [StartAnimationSystemParams](arkts-arkui-window-startanimationsystemparams-i-sys.md) |
| [WindowCreateParams](arkts-arkui-window-windowcreateparams-i-sys.md) |
| [Window](arkts-arkui-window-window-i-sys.md) |
| [SubWindowOptions](arkts-arkui-window-subwindowoptions-i-sys.md) |
| [WindowStage](arkts-arkui-window-windowstage-i-sys.md) |
| [SystemWindowOptions](arkts-arkui-window-systemwindowoptions-i-sys.md) |
| [ExtensionWindowConfig](arkts-arkui-window-extensionwindowconfig-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [WindowType](arkts-arkui-window-windowtype-e.md) |
| [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) |
| [SplitRatioPreference](arkts-arkui-window-splitratiopreference-e.md) |
| [WindowStatusType](arkts-arkui-window-windowstatustype-e.md) |
| [PixelUnit](arkts-arkui-window-pixelunit-e.md) |
| [WindowAnimationCurve](arkts-arkui-window-windowanimationcurve-e.md) |
| [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) |
| [AnimationType](arkts-arkui-window-animationtype-e.md) |
| [WindowAnchor](arkts-arkui-window-windowanchor-e.md) |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) |
| [RectChangeReason](arkts-arkui-window-rectchangereason-e.md) |
| [OcclusionState](arkts-arkui-window-occlusionstate-e.md) |
| [Orientation](arkts-arkui-window-orientation-e.md) |
| [OrientationExecutionResult](arkts-arkui-window-orientationexecutionresult-e.md) |
| [RotationChangeType](arkts-arkui-window-rotationchangetype-e.md) |
| [RectType](arkts-arkui-window-recttype-e.md) |
| [ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md) |
| [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) |
| [WindowEventType](arkts-arkui-window-windoweventtype-e.md) |
| [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) |
| [AcrossDisplayPresentation](arkts-arkui-window-acrossdisplaypresentation-e.md) |
| [GlobalWindowMode](arkts-arkui-window-globalwindowmode-e.md) |
| [WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md) |
| [WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md) |
| [ModalityType](arkts-arkui-window-modalitytype-e.md) |
| [WindowPostureMode](arkts-arkui-window-windowposturemode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [WindowType](arkts-arkui-window-windowtype-e-sys.md) |
| [WindowMode](arkts-arkui-window-windowmode-e-sys.md) |
| [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) |
| [AnimationType](arkts-arkui-window-animationtype-e-sys.md) |
| [BlurStyle](arkts-arkui-window-blurstyle-e-sys.md) |
| [ExtensionWindowAttribute](arkts-arkui-window-extensionwindowattribute-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md) | Describes a generic callback function for rotation event notifications.  In this callback function, the parameter type is [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), and the return value type is [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \\|
| [SpecificSystemBar](arkts-arkui-window-specificsystembar-t.md) |
