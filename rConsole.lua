local function postRequest(url, data)
    request({
        Url = "http://127.0.0.1:5000" .. url,
        Method = "POST",
        Headers = { ["Content-Type"] = "application/json" },
        Body = game:GetService("HttpService"):JSONEncode(data)
    })
end

getgenv().rconsoleprint = function(message, color)
    postRequest("/rconsoleprint", {message = message, color = color or "WHITE"})
end

getgenv().rconsoleinfo = function(message)
    postRequest("/rconsoleinfo", {message = message})
end

getgenv().rconsolewarn = function(message)
    postRequest("/rconsolewarn", {message = message})
end

getgenv().rconsoleerr = function(message)
    postRequest("/rconsoleerr", {message = message})
end

getgenv().rconsoleclear = function()
    postRequest("/rconsoleclear", {})
end

getgenv().rconsolename = function(title)
    postRequest("/rconsolename", {title = title})
end
