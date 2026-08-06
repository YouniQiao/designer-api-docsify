# WebNavigationType

Enum type supplied to \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ for the navigation's type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum WebNavigationType--><!--Device-unnamed-export declare enum WebNavigationType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

Unknown type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebNavigationType-UNKNOWN = 0--><!--Device-WebNavigationType-UNKNOWN = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## MAIN_FRAME_NEW_ENTRY

```TypeScript
MAIN_FRAME_NEW_ENTRY = 1
```

A new entry was created due to a navigation happened on the main frame.Contains all situations that will generate a mainframe navigation entry,which means that navigations to a hash on the same document or history.pushState also belong to this type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebNavigationType-MAIN_FRAME_NEW_ENTRY = 1--><!--Device-WebNavigationType-MAIN_FRAME_NEW_ENTRY = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## MAIN_FRAME_EXISTING_ENTRY

```TypeScript
MAIN_FRAME_EXISTING_ENTRY = 2
```

Navigate to an existing entry due to a navigation on the main frame.e.g.1. History navigations.2. Reloads (contains loading the same url).3. Same-document navigations(history.replaceState(), location.replace()).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebNavigationType-MAIN_FRAME_EXISTING_ENTRY = 2--><!--Device-WebNavigationType-MAIN_FRAME_EXISTING_ENTRY = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NAVIGATION_TYPE_NEW_SUBFRAME

```TypeScript
NAVIGATION_TYPE_NEW_SUBFRAME = 4
```

A navigation happened on subframe which was triggered by user.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebNavigationType-NAVIGATION_TYPE_NEW_SUBFRAME = 4--><!--Device-WebNavigationType-NAVIGATION_TYPE_NEW_SUBFRAME = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NAVIGATION_TYPE_AUTO_SUBFRAME

```TypeScript
NAVIGATION_TYPE_AUTO_SUBFRAME = 5
```

A navigation happened on the subframe automatically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebNavigationType-NAVIGATION_TYPE_AUTO_SUBFRAME = 5--><!--Device-WebNavigationType-NAVIGATION_TYPE_AUTO_SUBFRAME = 5-End-->

**System capability:** SystemCapability.Web.Webview.Core

