# WindowSnapshotConfiguration

Describes the configuration of the main window screenshot.

**Since:** 23

<!--Device-window-interface WindowSnapshotConfiguration--><!--Device-window-interface WindowSnapshotConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
```

## useCache

```TypeScript
useCache?: boolean
```

Whether the existing screenshot of the main window should be used. The default value is **true**. When it is set to **true**, the system uses the existing screenshot of the main window, or captures the latest screenshot if no existing screenshot is saved. When it is set to **false**, the system captures the latest screenshot of the main window.

**Type:** boolean

**Since:** 23

<!--Device-WindowSnapshotConfiguration-useCache?: boolean--><!--Device-WindowSnapshotConfiguration-useCache?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager
