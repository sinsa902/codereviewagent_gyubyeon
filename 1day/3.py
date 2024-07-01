def testableHtml(pageData, includeSuiteSetup):
    wikiPage = pageData.getWikiPage()
    buffer = []
    if pageData.hasAttribute("Test"):
        if includeSuiteSetup:
            suiteSetup = PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_SETUP_NAME, wikiPage
            )
            if suiteSetup != None:
                pagePath = suiteSetup.getPageCrawler().getFullPath(suiteSetup)
                pagePathName = PathParser.render(pagePath)
                buffer.append("!include -setup .")
                buffer.append(pagePathName)
                buffer.append("\\n")
        setup = PageCrawlerImpl.getInheritedPage("SetUp", wikiPage)
        if setup != None:
            setupPath = wikiPage.getPageCrawler().getFullPath(setup)
            setupPathName = PathParser.render(setupPath)
            buffer.append("!include -setup .")
            buffer.append(setupPathName)
            buffer.append("\\n")
    buffer.append(pageData.getContent())
    if pageData.hasAttribute("Test"):
        teardown = PageCrawlerImpl.getInheritedPage("TearDown", wikiPage)
        if teardown != None:
            teardownPath = suiteSetup.getPageCrawler().getFullPath(teardown)
            teardownPathName = PathParser.render(teardownPath)
            buffer.append("!include -teardown .")
            buffer.append(pagePathName)
            buffer.append("\\n")
        if includeSuiteSetup:
            suiteTeardown = PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_TEARDOWN_NAME, wikiPage
            )
            if suiteTeardown != None:
                pagePath = suiteSetup.getPageCrawler().getFullPath(suiteTeardown)
                pagePathName = PathParser.render(pagePath)
                buffer.append("!include -teardown .")
                buffer.append(pagePathName)
                buffer.append("\\n")
    pageData.setContent("".join(buffer))
    return pageData.getHtml()
