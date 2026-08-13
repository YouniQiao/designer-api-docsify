# window

Window manager.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace window--><!--Device-unnamed-declare namespace window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createWindow](arkts-arkui-window-createwindow-f.md#createWindow) | Creates a child window or system window. This API uses an asynchronous callback to return the result. In non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default. In freeform window mode, the child window created uses an immersive layout when [decorEnabled](arkts-arkui-window-configuration-i.md#Configuration) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**. |
| [createWindow](arkts-arkui-window-createwindow-f.md#createWindow) | Creates a child window or system window. This API uses a promise to return the result. In non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default. In freeform window mode, the child window created uses an immersive layout when [decorEnabled](arkts-arkui-window-configuration-i.md#Configuration) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**. |
| [create](arkts-arkui-window-create-f.md#create) | Creates a child window. This API uses an asynchronous callback to return the result. The child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default. |
| [create](arkts-arkui-window-create-f.md#create) | Creates a child window. This API uses a promise to return the result. The child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default. |
| [create](arkts-arkui-window-create-f.md#create) | Creates a system window. This API uses a promise to return the result. |
| [create](arkts-arkui-window-create-f.md#create) | Creates a system window. This API uses an asynchronous callback to return the result. |
| [find](arkts-arkui-window-find-f.md#find) | Finds a window based on the ID. This API uses an asynchronous callback to return the result. |
| [find](arkts-arkui-window-find-f.md#find) | Finds a window based on the ID. This API uses a promise to return the result. |
| [findWindow](arkts-arkui-window-findwindow-f.md#findWindow) | Finds a window based on the name. |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#getTopWindow) | Obtains the top window of the current application. This API uses an asynchronous callback to return the result. |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#getTopWindow) | Obtains the top window of the current application. This API uses a promise to return the result. |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#getTopWindow) | Obtains the top window of the current application. This API uses a promise to return the result. |
| [getTopWindow](arkts-arkui-window-gettopwindow-f.md#getTopWindow) | Obtains the top window of the current application. This API uses an asynchronous callback to return the result. |
| [getLastWindow](arkts-arkui-window-getlastwindow-f.md#getLastWindow) | Obtains the topmost layer child window of the current application. This API uses an asynchronous callback to return the result. If no child window exists or the child window is not displayed by calling [showWindow()](arkts-arkui-window-window-i.md#showWindow), the main window of the application is returned. |
| [getLastWindow](arkts-arkui-window-getlastwindow-f.md#getLastWindow) | Obtains the topmost layer child window of the current application. This API uses a promise to return the result. If no child window exists or the child window is not displayed by calling [showWindow()](arkts-arkui-window-window-i.md#showWindow), the main window of the application is returned. |
| [shiftAppWindowFocus](arkts-arkui-window-shiftappwindowfocus-f.md#shiftAppWindowFocus) | Shifts the window focus from the source window to the target window in the same application. The window focus can be shifted within the main window and child windows. This API uses a promise to return the result. Ensure that the target window can gain focus (configurable by calling [setWindowFocusable()](arkts-arkui-window-window-i.md#setWindowFocusable) ) and that [showWindow()](arkts-arkui-window-window-i.md#showWindow) has been successfully executed. > **NOTE：**> > Before calling **shiftAppWindowFocus()**, ensure that the target window has called > [loadContent()](arkts-arkui-window-window-i.md#loadContent) > or [setUIContent()](arkts-arkui-window-window-i.md#setUIContent) > and these operations have been effective. Otherwise, an invisible window may gain focus, causing function > exceptions or affecting user experience. |
| [shiftAppWindowPointerEvent](arkts-arkui-window-shiftappwindowpointerevent-f.md#shiftAppWindowPointerEvent) | Transfers a mouse input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result. To transfer mouse input events, the source window must call this API within the callback of the onTouch event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window. |
| [shiftAppWindowTouchEvent](arkts-arkui-window-shiftappwindowtouchevent-f.md#shiftAppWindowTouchEvent) | Transfers a touchscreen input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result. To transfer touchscreen input events, the source window must call this API within the callback of the onTouch event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window. |
| [getWindowsByCoordinate](arkts-arkui-window-getwindowsbycoordinate-f.md#getWindowsByCoordinate) | Obtains visible windows at the specified coordinates within the current application, sorted by their current layer order. The window at the topmost layer corresponds to index 0 of the array. This API uses a promise to return the result. |
| [getAllWindowLayoutInfo](arkts-arkui-window-getallwindowlayoutinfo-f.md#getAllWindowLayoutInfo) | Obtains the layout information array of all windows visible on a display. The layout information is arranged based on the current window stacking order, and the topmost window in the hierarchy is at index 0 of the array. This API uses a promise to return the result. |
| [getAllWindowLayoutInfo](arkts-arkui-window-getallwindowlayoutinfo-f.md#getAllWindowLayoutInfo) | Obtains the array of window layout info visible on a specified screen. The width and height of each rect are calculated after scaling. The array is sorted by the current window level. The index of the array corresponding to the highest level is 0. |
| [getGlobalWindowMode](arkts-arkui-window-getglobalwindowmode-f.md#getGlobalWindowMode) | Obtains the window mode of the window that is in the foreground lifecycle on the specified screen. This API uses a promise to return the result. |
| [onApplicationFocusStateChange](arkts-arkui-window-onapplicationfocusstatechange-f.md#onApplicationFocusStateChange) | Register the callback for application process focus state changes. |
| [offApplicationFocusStateChange](arkts-arkui-window-offapplicationfocusstatechange-f.md#offApplicationFocusStateChange) | Unregister the callback for application process focus state changes. |
| [setStartWindowBackgroundColor](arkts-arkui-window-setstartwindowbackgroundcolor-f.md#setStartWindowBackgroundColor) | Sets the background color of the splash screen of the UIAbility based on the specified module name and ability name within the same bundle name. This API uses a promise to return the result. This API takes effect for all processes of the same bundle name, for example, in multi-instance or clone scenarios. |
| [setWatermarkImageForAppWindows](arkts-arkui-window-setwatermarkimageforappwindows-f.md#setWatermarkImageForAppWindows) | Sets a watermark image for windows in the current application process. This API uses a promise to return the result. This API must be called after [loadContent()](arkts-arkui-window-window-i.md#loadContent) or [setUIContent()](arkts-arkui-window-window-i.md#setUIContent) takes effect. |
| [getAllMainWindowInfo](arkts-arkui-window-getallmainwindowinfo-f.md#getAllMainWindowInfo) | Obtains the information about all main windows. This API uses a promise to return the result. |
| [getMainWindowSnapshot](arkts-arkui-window-getmainwindowsnapshot-f.md#getMainWindowSnapshot) | Obtains the screenshots of one or more main windows specified by **windowId**. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createSubWindowAndBindParent](arkts-arkui-window-createsubwindowandbindparent-f-sys.md#createSubWindowAndBindParent) | Create a subwindow with a specific name and bind parent. The parent window only supports main window. The subwindow follows the parent window to show/hide, but does not follow the parent window to destroy. The subwindow listens to the parent window lifecycle changes through the callback function. |
| [minimizeAll](arkts-arkui-window-minimizeall-f-sys.md#minimizeAll) | Minimizes all main windows on a display. |
| [minimizeAll](arkts-arkui-window-minimizeall-f-sys.md#minimizeAll-(System-API)) | Minimizes all main windows on a display. This API uses a promise to return the result. |
| [minimizeAllWithExclusion](arkts-arkui-window-minimizeallwithexclusion-f-sys.md#minimizeAllWithExclusion) | Minimizes all main windows on a display while keeping one window open. This API uses a promise to return the result. |
| [toggleShownStateForAllAppWindows](arkts-arkui-window-toggleshownstateforallappwindows-f-sys.md#toggleShownStateForAllAppWindows) | Hides or restores the application's windows during quick multi-window switching. This API uses an asynchronous callback to return the result. |
| [toggleShownStateForAllAppWindows](arkts-arkui-window-toggleshownstateforallappwindows-f-sys.md#toggleShownStateForAllAppWindows-(System-API)) | Hides or restores the application's windows during quick multi-window switching. This API uses a promise to return the result. |
| [setWindowLayoutMode](arkts-arkui-window-setwindowlayoutmode-f-sys.md#setWindowLayoutMode) | Sets the window layout mode. This API uses an asynchronous callback to return the result. |
| [setWindowLayoutMode](arkts-arkui-window-setwindowlayoutmode-f-sys.md#setWindowLayoutMode-(System-API)) | Sets the window layout mode. This API uses a promise to return the result. |
| [setGestureNavigationEnabled](arkts-arkui-window-setgesturenavigationenabled-f-sys.md#setGestureNavigationEnabled) | Enables or disables gesture navigation. This API uses an asynchronous callback to return the result. For security purposes, the system does not interfere with the disabling and enabling of gesture navigation. If an application exits abnormally after it disables gesture navigation and wants to restore gesture navigation, it must implement automatic launch and call this API again to enable gesture navigation. |
| [setGestureNavigationEnabled](arkts-arkui-window-setgesturenavigationenabled-f-sys.md#setGestureNavigationEnabled-(System-API)) | Enables or disables gesture navigation. This API uses a promise to return the result. For security purposes, the system does not interfere with the disabling and enabling of gesture navigation. If an application exits abnormally after it disables gesture navigation and wants to restore gesture navigation, it must implement automatic launch and call this API again to enable gesture navigation. |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setWaterMarkImage) | Controls whether a watermark image is displayed on the screen. This API uses a promise to return the result. |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setWaterMarkImage-(System-API)) | Set watermark image. |
| [setWaterMarkImage](arkts-arkui-window-setwatermarkimage-f-sys.md#setWaterMarkImage-(System-API)) | Controls whether a watermark image is displayed on the screen. This API uses an asynchronous callback to return the result. |
| [setSpecificSystemWindowZIndex](arkts-arkui-window-setspecificsystemwindowzindex-f-sys.md#setSpecificSystemWindowZIndex) | Sets the z-level of a system window. This API uses a promise to return the result. Adjusts the **zIndex** of all system windows of the specified type to the configured value. Before and after the adjustment, the relative z-level of these windows remains unchanged, and the focus window does not change. After the application is closed, the z-level of specified windows is restored to the default value. You are advised to set different **zIndex** values for different types of windows. If there are windows with the same **zIndex**, the relative z-level of windows remains unchanged before and after the setting. |
| [getVisibleWindowInfo](arkts-arkui-window-getvisiblewindowinfo-f-sys.md#getVisibleWindowInfo) | Obtains information about visible main windows on the current screen. Visible main windows are main windows that are not returned to the background. This API uses a promise to return the result. |
| [getTopNavDestinationName](arkts-arkui-window-gettopnavdestinationname-f-sys.md#getTopNavDestinationName) | Obtains the name of NavDestination in the current top-level Navigation component of the specified foreground window. This API uses a promise to return the result. |
| [getSnapshot](arkts-arkui-window-getsnapshot-f-sys.md#getSnapshot) | Obtains a snapshot of the same size as the specified window. This API uses a promise to return the result. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](arkts-arkui-window-window-i.md#setWindowPrivacyMode) ), taking a screenshot will result in a blank screen. |
| on_systemBarTintChange | Subscribes to the property change event of the status bar and navigation bar. |
| [onSystemBarTintChange](arkts-arkui-window-onsystembartintchange-f-sys.md#onSystemBarTintChange) | Subscribes to the property change event of the status bar and navigation bar. |
| off_systemBarTintChange | Unsubscribes from the property change event of the status bar and navigation bar. |
| [offSystemBarTintChange](arkts-arkui-window-offsystembartintchange-f-sys.md#offSystemBarTintChange) | Unsubscribes from the property change event of the status bar and navigation bar. |
| on_gestureNavigationEnabledChange | Subscribes to the gesture navigation status change event. |
| [onGestureNavigationEnabledChange](arkts-arkui-window-ongesturenavigationenabledchange-f-sys.md#onGestureNavigationEnabledChange) | Subscribes to the gesture navigation status change event. |
| off_gestureNavigationEnabledChange | Unsubscribes from the gesture navigation status change event. |
| [offGestureNavigationEnabledChange](arkts-arkui-window-offgesturenavigationenabledchange-f-sys.md#offGestureNavigationEnabledChange) | Unsubscribes from the gesture navigation status change event. |
| on_waterMarkFlagChange | Subscribes to the watermark status change event. |
| [onWaterMarkFlagChange](arkts-arkui-window-onwatermarkflagchange-f-sys.md#onWaterMarkFlagChange) | Subscribes to the watermark status change event. |
| off_waterMarkFlagChange | Unsubscribes from the watermark status change event. |
| [offWaterMarkFlagChange](arkts-arkui-window-offwatermarkflagchange-f-sys.md#offWaterMarkFlagChange) | Unsubscribes from the watermark status change event. |
| [notifyScreenshotEvent](arkts-arkui-window-notifyscreenshotevent-f-sys.md#notifyScreenshotEvent) | Notifies a screenshot event. This API uses a promise to return the result. |
| [moveMainWindowToTargetDisplay](arkts-arkui-window-movemainwindowtotargetdisplay-f-sys.md#moveMainWindowToTargetDisplay) | Move a window to the target display. The window must be a main window. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | Describes the properties of the status bar&lt;!--Del--&gt; and three-button navigation bar&lt;!--DelEnd--&gt;. |
| [StatusBarProperty](arkts-arkui-window-statusbarproperty-i.md) | Describes the properties of the status bar. These properties are returned when you query the status bar's configuration details. |
| [SystemBarStyle](arkts-arkui-window-systembarstyle-i.md) | Describes the properties of the status bar. These properties are valid for the page-level status bar. |
| [FrameMetrics](arkts-arkui-window-framemetrics-i.md) | Enumerates the metrics for frame performance. |
| [Rect](arkts-arkui-window-rect-i.md) | Describes the rectangular area of the window. |
| [RectInVP](arkts-arkui-window-rectinvp-i.md) | Describes the rectangular area of the window, in vp. |
| [Position](arkts-arkui-window-position-i.md) | Describes the position of the window or component. |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) | Describes the area to avoid for window content. When adapting window content for an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout), you should adjust the content based on the corresponding **AvoidArea** specified by [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType). In the avoid area, the application window content is obscured and does not respond to user click events. > **NOTE：**> > The figure below shows the meanings of **leftRect**, **topRect**, **rightRect**, and **bottomRect**. > >  |
| [UIEnvAvoidAreaVP](arkts-arkui-window-uienvavoidareavp-i.md) | Describes the information about the window avoidance area in units of vp, which requires careful attention during [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) adaptation. |
| [Size](arkts-arkui-window-size-i.md) | Describes the window size, in px. |
| [SizeInVP](arkts-arkui-window-sizeinvp-i.md) | Describes the window size, in vp. |
| [WindowInfo](arkts-arkui-window-windowinfo-i.md) | Describes the window information. |
| [WindowDensityInfo](arkts-arkui-window-windowdensityinfo-i.md) | Describes the information about the display density of the screen where the window is located and the window's custom display density. It is a scale factor independent of pixel units, that is, a factor for scaling display size. |
| [WindowProperties](arkts-arkui-window-windowproperties-i.md) | Describes the window properties. |
| [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) | Describes the button style of the system decoration bar. |
| [Configuration](arkts-arkui-window-configuration-i.md) | Defines the parameters for creating a child window or system window. |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) | Describes the parameters for window size limits. Applications can obtain the current window size limits (in px) via [getWindowLimits](arkts-arkui-window-window-i.md#getWindowLimits). Starting from API version 22, they can also be obtained via [getWindowLimitsVP](arkts-arkui-window-window-i.md#getWindowLimitsVP) (in vp). The actual window size limits applied are determined by the intersection of the default system limits, application configurations, and runtime settings, with the priority (from highest to lowest) as follows: 1. Window size limits configured by the application via [setWindowLimits](arkts-arkui-window-window-i.md#setWindowLimits). 2. Window size limits specified by the application via [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md#StartOptions) when the application starts the window through [startAbility](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#startAbility). (This approach is supported since API version 17.) 3. Window size limits configured by the application in [abilities in the module.json5 file](../../../quick-start/module-configuration-file.md#abilities). 4. Default system limits (which vary depending on the product and window type). > **NOTE：**> > For the **maxWidth**, **maxHeight**, **minWidth**, and **minHeight** properties: > > - The default unit is px. Starting from API version 22, the unit can be px or vp, depending on the setting of > **pixelUnit**. > > - The value is an integer. Floating-point values will be rounded down. > > - The default value is **0**, indicating that the property does not change. > > - The lower bound of the effective range is the minimum height/width limited by the system. > > - The upper bound of the effective range is the maximum height/width limited by the system. |
| [TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md) | Describes the rectangle used to hold the minimize, maximize, and close buttons on the title bar. This rectangle is located in the top-right corner of the window. |
| [RectChangeOptions](arkts-arkui-window-rectchangeoptions-i.md) | Describes the value and reason returned upon a window rectangle (position and size) change. |
| [AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md) | Describes the new area where the window cannot be displayed. The new area is returned when the corresponding event is triggered. |
| [UIEnvWindowAvoidAreaInfoPX](arkts-arkui-window-uienvwindowavoidareainfopx-i.md) | Describes [environment variable](../../../ui/arkts-env-system-property.md) data types for window avoidance areas of different types. All types of window avoidance areas are measured in px. |
| [UIEnvWindowAvoidAreaInfoVP](arkts-arkui-window-uienvwindowavoidareainfovp-i.md) | Describes [environment variable](../../../ui/arkts-env-system-property.md) data types for window avoidance areas of different types. All types of window avoidance areas are measured in vp. |
| [MainWindowInfo](arkts-arkui-window-mainwindowinfo-i.md) | Describes the main window information. |
| [WindowSnapshotConfiguration](arkts-arkui-window-windowsnapshotconfiguration-i.md) | Describes the configuration of the main window screenshot. |
| [OrientationResult](arkts-arkui-window-orientationresult-i.md) | Result of setting preferred orientation |
| [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md) | Describes the window information obtained during window rotation changes. |
| [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) | Describes the information returned by the application during window rotation changes. The system uses the information to adjust the size of the current window rectangle. If the returned information is about the rotation change of the main window, the system does not change the size of the main window. There are limitations on the size of application windows and system windows. For details about specific restrictions and rules, see [resize](arkts-arkui-window-window-i.md#resize). |
| [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md) | Describes the configuration for window animation. |
| [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) | Describes the window transition animation. |
| [MaximizeOptions](arkts-arkui-window-maximizeoptions-i.md) | Optional configuration for maximizing. |
| [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) | Describes the window movement configuration. |
| [StartAnimationParams](arkts-arkui-window-startanimationparams-i.md) | Describes the parameters for the startup animation. The configuration is valid only for transitions between different abilities within the same application. The configuration is valid only full-screen applications. |
| [WindowCreateParams](arkts-arkui-window-windowcreateparams-i.md) | Describes the window parameters during application startup. |
| [WindowSnapshotAnimationConfig](arkts-arkui-window-windowsnapshotanimationconfig-i.md) | Configuration for window snapshot animation. |
| [KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md) | Describes the information about the soft keyboard window. |
| [KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md) | Describes the configuration for keyframe policies. |
| [Window](arkts-arkui-window-window-i.md) | Represents a window instance, which is the basic unit managed by the window manager. In the following API examples, you must use [getLastWindow()](arkts-arkui-window-getlastwindow-f.md#getLastWindow), [createWindow()](arkts-arkui-window-createwindow-f.md#createWindow), or [findWindow()](arkts-arkui-window-findwindow-f.md#findWindow) to obtain a Window instance (named windowClass in this example) and then call a method in this instance. |
| [ShowWindowOptions](arkts-arkui-window-showwindowoptions-i.md) | Describes the parameters for displaying a child window or system window. |
| [SubWindowOptions](arkts-arkui-window-subwindowoptions-i.md) | Describes the parameters used for creating a child window. |
| [WindowStage](arkts-arkui-window-windowstage-i.md) | Implements a window manager, which manages each basic window unit, that is, [Window](#window) instance. Before calling any of the following APIs, you must use [onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) to create a WindowStage instance. |
| [WindowLayoutInfo](arkts-arkui-window-windowlayoutinfo-i.md) | Describes the information about the window layout. |
| [WindowInfoOptions](arkts-arkui-window-windowinfooptions-i.md) | Filter criteria for window information. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [SystemBarRegionTint](arkts-arkui-window-systembarregiontint-i-sys.md) | Describes the callback for a single system bar. |
| [SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md) | Describes the callback for the current system bar. |
| [WindowAnchorInfo](arkts-arkui-window-windowanchorinfo-i-sys.md) | Describes the anchor point information used to maintain the relative position between the level-1 child window and the main window. |
| [SubWindowAttachOptions](arkts-arkui-window-subwindowattachoptions-i-sys.md) | Describes the parameters used to maintain the relative position between the child window and the main window. |
| [WindowInfo](arkts-arkui-window-windowinfo-i-sys.md) | Describes the window information. |
| [ScaleOptions](arkts-arkui-window-scaleoptions-i-sys.md) | Describes the scale parameters. |
| [RotateOptions](arkts-arkui-window-rotateoptions-i-sys.md) | Describes the rotation parameters. |
| [TranslateOptions](arkts-arkui-window-translateoptions-i-sys.md) | Describes the translation parameters. |
| [TransitionContext](arkts-arkui-window-transitioncontext-i-sys.md) | Provides the context for the transition animation. |
| [TransitionController](arkts-arkui-window-transitioncontroller-i-sys.md) | Implements the transition animation controller. Before calling any API, you must create a system window. For details, see the sample code. |
| [Configuration](arkts-arkui-window-configuration-i-sys.md) | Defines the parameters for creating a child window or system window. |
| [StartMovingOptions](arkts-arkui-window-startmovingoptions-i-sys.md) | Optional configuration for startMovingWithOptions. |
| [StartAnimationSystemParams](arkts-arkui-window-startanimationsystemparams-i-sys.md) | Describes the start animation configuration. This API works only for full-screen applications. The configuration does not take effect for inter-application transitions, where the default animation of the system is used. |
| [WindowCreateParams](arkts-arkui-window-windowcreateparams-i-sys.md) | Describes the window parameters during application startup. |
| [Window](arkts-arkui-window-window-i-sys.md) | Represents a window instance, which is the basic unit managed by the window manager. In the following API examples, you must use [getLastWindow()](arkts-arkui-window-getlastwindow-f.md#getLastWindow), [createWindow()](arkts-arkui-window-createwindow-f.md#createWindow), or [findWindow()](arkts-arkui-window-findwindow-f.md#findWindow) to obtain a Window instance (named windowClass in this example) and then call a method in this instance. |
| [SubWindowOptions](arkts-arkui-window-subwindowoptions-i-sys.md) | Describes the parameters used for creating a child window. |
| [WindowStage](arkts-arkui-window-windowstage-i-sys.md) | Implements a window manager, which manages each basic window unit, that is, [Window](#window) instance. Before calling any of the following APIs, you must use [onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) to create a WindowStage instance. |
| [SystemWindowOptions](arkts-arkui-window-systemwindowoptions-i-sys.md) | Describes the parameters for creating a system window. |
| [ExtensionWindowConfig](arkts-arkui-window-extensionwindowconfig-i-sys.md) | Describes the parameters for creating a window for a UI ServiceExtensionAbility. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [WindowType](arkts-arkui-window-windowtype-e.md) | Enumerates the window types. |
| [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | Enumerates the types of areas to avoid for window content. When adapting window content for an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout), you should adjust the content based on the corresponding [AvoidArea](arkts-arkui-window-avoidarea-i.md#AvoidArea) specified by **AvoidAreaType**. |
| [SplitRatioPreference](arkts-arkui-window-splitratiopreference-e.md) | Describes the type of split ratio preference. |
| [WindowStatusType](arkts-arkui-window-windowstatustype-e.md) | Enumerates the window modes. |
| [PixelUnit](arkts-arkui-window-pixelunit-e.md) | Enumerates the pixel units. You can use px2vp and vp2px to convert between physical pixels and virtual pixels. |
| [WindowAnimationCurve](arkts-arkui-window-windowanimationcurve-e.md) | Enumerates the types of window animation curves. |
| [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) | Enumerates the types of window transition animations. |
| [AnimationType](arkts-arkui-window-animationtype-e.md) | Enumerates the types of window animations. |
| [WindowAnchor](arkts-arkui-window-windowanchor-e.md) | Enumerates the window anchor points. |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) | Enumerates the color spaces. |
| [RectChangeReason](arkts-arkui-window-rectchangereason-e.md) | Enumerates the reasons for window rectangle (position and size) changes. |
| [OcclusionState](arkts-arkui-window-occlusionstate-e.md) | Enumerates the window visibility states. |
| [Orientation](arkts-arkui-window-orientation-e.md) | Enumerates the window orientations. &lt;!--Del--&gt;For details of the differences between different enumerated values, see [What is the difference between orientation values 8 to 10 or 12 and values 13 to 16 (API version 9)](../../../faqs/faqs-window-manager.md#what-is-the-difference-between-orientation-values-8-to-10-or-12-and-values-13-to-16-api-version-9) .&lt;!--DelEnd--&gt; |
| [OrientationExecutionResult](arkts-arkui-window-orientationexecutionresult-e.md) | Type of execution result of setting preferred orientation |
| [RotationChangeType](arkts-arkui-window-rotationchangetype-e.md) | Enumerates the types of window rotation events. |
| [RectType](arkts-arkui-window-recttype-e.md) | Enumerates the types of window rectangle coordinate systems. |
| [ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md) | Enumerates the screenshot event types. |
| [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) | Enumerates the types of rotation information. |
| [WindowEventType](arkts-arkui-window-windoweventtype-e.md) | Enumerates the window lifecycle states. |
| [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) | Enumerates the layout when the window is maximized. |
| [AcrossDisplayPresentation](arkts-arkui-window-acrossdisplaypresentation-e.md) | Enum for across-display policy used when maximizing in the half-folded state of a foldable 2-in-1 device. |
| [GlobalWindowMode](arkts-arkui-window-globalwindowmode-e.md) | Enumerates the window modes. |
| [WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md) | Enumerates the lifecycle event types of a WindowStage. |
| [WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md) | Enumerates the lifecycle state types of a WindowStage. |
| [ModalityType](arkts-arkui-window-modalitytype-e.md) | Enumerates the modality types of the child window. |
| [WindowPostureMode](arkts-arkui-window-windowposturemode-e.md) | Enumerates of window posture mode. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [WindowType](arkts-arkui-window-windowtype-e-sys.md) | Enumerates the window types. |
| [WindowMode](arkts-arkui-window-windowmode-e-sys.md) | Enumerates the window modes. |
| [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | Enumerates the window layout modes. |
| [AnimationType](arkts-arkui-window-animationtype-e-sys.md) | Enumerates the types of window animations. |
| [BlurStyle](arkts-arkui-window-blurstyle-e-sys.md) | Enumerates the window blur styles. |
| [ExtensionWindowAttribute](arkts-arkui-window-extensionwindowattribute-e-sys.md) | Enumerates the attributes of a window for a UI ServiceExtensionAbility. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md) | Describes a generic callback function for rotation event notifications. In this callback function, the parameter type is [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md#RotationChangeInfo) , and the return value type is [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#RotationChangeResult) \\| void. |
| [SpecificSystemBar](arkts-arkui-window-specificsystembar-t.md) | Defines the type of system bar that can be displayed or hidden. |

