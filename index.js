/**
 * This is the main entrypoint to your Probot app
 * @param {import('probot').Probot} app
 */
module.exports = (app) => {
  // Your code here
  app.log.info("Yay, the app was loaded!");

  app.on("issues.opened", async (context) => {
    const issueComment = context.issue({
      body: "Thanks for opening this issue!",
    });
    return context.octokit.issues.createComment(issueComment);
  });

  app.on('push', async context => {
    const branch = context.payload.ref.split('/').pop();

    if (branch !== 'dev') {
        return;
    }

    const pr = {
        owner: context.repo.owner,
        repo: context.repo.repo,
        title: `PR from ${branch} to main`,
        head: branch,
        base: 'main',
        body: 'Auto-generated PR'
    };

    await context.github.pulls.create(pr);
});

  // For more information on building apps:
  // https://probot.github.io/docs/

  // To get your app running against GitHub, see:
  // https://probot.github.io/docs/development/
};
